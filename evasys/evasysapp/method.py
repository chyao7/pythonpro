import math
import pandas as pd
import numpy as np
import datetime

class EvalCalc:

	def __init__(self, datas, companies):
		self.datas = datas
		self.companies = companies
        
	#数据标准化
	def standard(self, data):
		datas = []
		for i in data:
			std_i = (i - data.min()) / (data.max() - data.min())
			std_i = np.round(std_i,3)
			datas.append(std_i)
		return datas
	
	def standard2(self, data):
		datas = []
		for i in data:
			std_i = ((i - data.min()) / (data.max() - data.min() + 0.1) * 20 + 80)
			std_i = np.round(std_i,2)
			datas.append(std_i)
		return datas
    
	#读指标数据
	def readData(self):
		new_data = []
		first_index = {}
		second_index = {}
		for i,dic in enumerate(self.datas):
			if i == 0:
				for k,v in dic.items():
					if k[:2] not in first_index:
						first_index[k[:2]] = v[0]
					if k[2:4] not in second_index:
						second_index[k[2:4]] = v[1]
			d = {}
			for k,v in dic.items():
				d[k] = float(v[3])
			new_data.append(d)
		data = pd.DataFrame(new_data)
		index_lst = data.columns
		standard_data = data.copy()     
		for i in range(len(index_lst)):
			standard_data[index_lst[i]] = self.standard(standard_data[index_lst[i]])
		return np.array(standard_data), index_lst, first_index, second_index

	#权重计算（熵权法）
	def calc_weight(self, array):
		for i in range(array.shape[1]):
			sum_ = np.sum(array[:,i])
			for j in range(len(array[:,i])):
				array[j,i] = np.round(array[j,i] / sum_,3)
		e_lst = []
		k = 1 / math.log(array.shape[0])
		
		for i in range(array.shape[1]):
			e = 0
			for j in range(len(array[:,i])):
				if array[j,i] == 0:
					e += 0
				else:
					e += array[j,i] * math.log(array[j,i])
			e = round(-k * e,3)
			e_lst.append(e)
		
		d_lst = [1] * len(e_lst)
		d_lst = list(map(lambda x:round(x[0] - x[1],3),zip(d_lst,e_lst)))
		weights = np.round(d_lst / sum(d_lst),3)
		return weights
	
	#分级评价结果计算（使用熵权法计算得出的客观权重）
	def sim_evaluate(self, array_lst, first_index, second_index):
		all_ = []
		index_dic = [first_index,second_index,{'100':'总得分'}]      
		for m, array1_lst in enumerate(array_lst):
			score_lst = []
			target = index_dic[m]
			length = len(array1_lst)
			for k,v in array1_lst.items():
				weights = self.calc_weight(v)
				weights = np.array(weights)
				weights = weights.reshape(-1,1)

				mean_lst = []
				for j in range(v.shape[1]):
					mean = np.round(v[:,j].mean(),4)
					mean_lst.append(mean)
				std_arr = v / mean_lst
				score = np.round(np.dot(std_arr,weights),3).tolist()

				dic = {}
				city_name = self.companies

				for i in range(len(score)):
					dic[city_name[i]] = score[i][0]
				sort_score = sorted(dic.items(),key = lambda x:x[1],reverse = True)
				sort_score = pd.DataFrame(sort_score)
				sort_score.columns = ['城市',target[k]]
				score_lst.append(sort_score)
			all_score = pd.DataFrame(city_name,columns=['城市'])
			for score in score_lst:
				all_score = pd.merge(all_score,score,on='城市')
			all_.append(all_score)
		return all_
	
	
	#数据集的切分（对应二级、一级和全部指标的数据集）
	def data_split(self, data, index_lst):
		val_1 = '00'
		first_lst = {}
		second_lst = {}       
		final_lst = {}
		sign_1 = 0
		for i,v in enumerate(index_lst):
			if val_1 != v[:2]:
				if type(data) == np.ndarray:
					first_lst[val_1] = data[:,sign_1:i]
				elif type(data) == list:
					first_lst[val_1] = data[sign_1:i]
				sign_1 = i
				val_1 = v[:2]
			else:
				continue
		if type(data) == np.ndarray:
			first_lst[val_1] = data[:,sign_1:data.shape[1]]
		elif type(data) == list:
			first_lst[val_1] = data[sign_1:len(data)]    
		val_2 = '00'
		sign_2 = 0
		for i,v in enumerate(index_lst):
			if val_2 != v[2:4]:
				if type(data) == np.ndarray:
					second_lst[val_2] = data[:,sign_2:i]
				elif type(data) == list:
					second_lst[val_2] = data[sign_2:i]
				sign_2 = i
				val_2 = v[2:4]
			else:
				continue
		if type(data) == np.ndarray:
			second_lst[val_2] = data[:,sign_2:data.shape[1]]
		elif type(data) == list:
			second_lst[val_2] = data[sign_2:len(data)]  
		final_lst['100'] = data
		return [first_lst,second_lst,final_lst]
		
	#API
	def excute(self):
		array1, index_lst, first_index, second_index = self.readData()
		np_weight = self.calc_weight(array1)
		#df_weight = pd.DataFrame(np_weight,index=columns.tolist(),columns=['权重'])
		#df_weight.to_excel(self.year+'客观指标权重.xlsx')
		array_lst = self.data_split(array1, index_lst)
		score = self.sim_evaluate(array_lst, first_index, second_index)
		opt_scores = []
		for s in score:   
			opt_score = s.set_index('城市')
			cols = opt_score.columns          
			for i in range(len(cols)):
				opt_score[cols[i]] = self.standard2(opt_score[cols[i]])
			opt_scores.append(opt_score)         
		return opt_scores
	
	
	
	