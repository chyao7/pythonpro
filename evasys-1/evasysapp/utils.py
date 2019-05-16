import pandas as pd
import numpy as np
from sympy import *
from sympy.abc import x
import json

class ExtAssMethod:
    def __init__(self, dataJson, jingDianYuList):
        self.dataJson = dataJson
        self.jingDianYuList = jingDianYuList
    def extendJingDianYu(self, jingDianYuList, direction = "left"):
        if direction=="left":
            negativePoint = jingDianYuList[0]-(jingDianYuList[2]-jingDianYuList[1])
            jingDianYuList.insert(0, negativePoint)
        elif direction=="right":
            advancePoint = jingDianYuList[-1]+(jingDianYuList[-2]-jingDianYuList[-3])
            jingDianYuList.append(advancePoint)
        else:
            pass
        return jingDianYuList

    def getJieYuTuple(self, jingDianYuList):
        return (min(jingDianYuList), max(jingDianYuList))

    def testData(self):
        if isinstance(self.jingDianYuList, list):
            flag = 0
        else:
            flag = 1
        if isinstance(self.dataJson, dict):
            flag = 0
        else:
            flag = 1
        return flag

    def addressIntervalData(self,jingDianYuList):
        return (tuple(((jingDianYuList[i] + jingDianYuList[i+1])/2,
                      (jingDianYuList[i+1] - jingDianYuList[i])/2) for i in range(len(jingDianYuList)-1)),
                tuple((jingDianYuList[i], jingDianYuList[i+1]) for i in range(len(jingDianYuList)-1)))

    def extDistance(self, singleJingDianYuTuple, singleEvaDataNum):
        return abs(singleEvaDataNum-((singleJingDianYuTuple[0]+singleJingDianYuTuple[1])*0.99)/2)\
               -(singleJingDianYuTuple[1]-singleJingDianYuTuple[0])/2

    def extWeight(self, jingDianYuTuple, evaDataList):
        absoluteWeightTuple =  tuple(tuple((2*(x-y[0])+0.1)/(y[1]-y[0]) if x<(y[0]+y[1])/2 else (2*(y[1]-x)+0.1)/(y[1]-y[0]) for y in jingDianYuTuple) for x in evaDataList)
        maxAbsoluteWeightNP = np.max(np.array(absoluteWeightTuple), axis = 1)
        relativeWeightNP = maxAbsoluteWeightNP/sum(maxAbsoluteWeightNP)
        return relativeWeightNP

    def correlation(self, jingDianYuTuple, jieYuTuple, evaDataList):
        return tuple(tuple(self.extDistance(singleJingDianYu, singleEvaNum)/(self.extDistance(jieYuTuple,singleEvaNum)-self.extDistance(singleJingDianYu,singleEvaNum)+singleJingDianYu[0]-singleJingDianYu[1]) \
                     if singleEvaNum<= singleJingDianYu[1] and singleEvaNum>singleJingDianYu[0] else \
                     self.extDistance(singleJingDianYu, singleEvaNum)/(self.extDistance(jieYuTuple,singleEvaNum)-self.extDistance(singleJingDianYu,singleEvaNum)) \
                 for singleJingDianYu in jingDianYuTuple) for singleEvaNum in evaDataList)

    def totalCorrelation(self, correlationNP, relativeWeightNP):
        """
        :param correlationNP: (number of evaluation data, number of jingdianyu)
        :param relativeWeightNP: (1,number of evaluation data)
        :return: totalCorelationNP,()
        """
        return np.dot(relativeWeightNP, correlationNP)

    def _checkData(self,minLimit,maxLimit,data):
        if data is not None:
            if minLimit<=data and data<=maxLimit:
                return True
            elif data<minLimit:
                print("数据值小于最低下限", data, minLimit)
                return False
            else :
                print("数据值大于最大上限", data, maxLimit)
                return False
        else:
            return False

    def checkData(self, x1, x2, x3, maxCorrelaiton, *limits):

        if maxCorrelaiton>0:
            if len(limits)==3:
                minLimit, middleLimit, maxLimit = limits
                if not self._checkData(minLimit, middleLimit, x1):
                    x1 = None
                else:
                    pass
                if not self._checkData(middleLimit, maxLimit, x2):
                    x2 = None
                else:
                    pass
            elif len(limits)==4:
                minLimit, middle1Limit, middle2Limit, maxLimit = limits
                if not self._checkData(minLimit, middle1Limit, x1):
                    x1 = None
                else:
                    pass
                if not self._checkData(middle1Limit, middle2Limit, x2):
                    x2 = None
                else:
                    pass
                if not self._checkData(middle2Limit, maxLimit, x3):
                    x3 = None
                else:
                    pass
            else:
                pass
        else:
            pass
        return x1,x2,x3


    def checkCommonEndPoint(self, tuple1, tuple2):
        if tuple1[0]==tuple2[0] :
            return 0
        else:
            if tuple1[1]==tuple2[1]:
                return 1
            else:
                return False


    def subExcuteTotalCorrelation(self, jingDianYuList, evaDataList):

        computeJingDianYuTuple, jingDianYuTuple = self.addressIntervalData(jingDianYuList)

        jieYuTuple = self.getJieYuTuple(jingDianYuList)

        relativeWeightTuple = self.extWeight(jingDianYuTuple,evaDataList)

        correlationTuple = self.correlation(jingDianYuTuple, jieYuTuple, evaDataList)

        correlationMat = np.matrix(correlationTuple)
        relativeWeightMat = np.matrix(relativeWeightTuple)
        totalCorrelationMat = self.totalCorrelation(correlationMat, relativeWeightMat)

        totalCorrelationNP = np.asarray(totalCorrelationMat).reshape(totalCorrelationMat.shape[1])

        return totalCorrelationNP, jingDianYuTuple


    def totalScore(self, totalCorrelationNp, jingDianYuTuple, jieYuTuple, evaDataList):


        jingDianYuIndexNP = int(np.argmax(totalCorrelationNp))

        belongJinDianYuTuple = jingDianYuTuple[jingDianYuIndexNP]
        maxCorrelationNum = np.max(totalCorrelationNp)

        aStar,bStar = belongJinDianYuTuple[0],belongJinDianYuTuple[1]
        a,b = jieYuTuple[0], jieYuTuple[1]

        if bStar<=(a+b)/2:
            x1 = solve(((aStar+bStar)/2-x-(bStar-aStar)/2)/(
                    (a+b)/2-x-(b-a)/2-((bStar+aStar)/2-x)-(bStar-aStar)/2))
            x2 = solve((x-(aStar+bStar)/2-(bStar-aStar)/2)/(
                    (a+b)/2-x-(b-a)/2-(x-(bStar+aStar)/2)-(bStar-aStar)/2))
            x3 = None



            x1Num, x2Num, x3Num = self.checkData(x1[0],x2[0], x3, maxCorrelationNum, aStar, (aStar+bStar)/2, bStar)

        elif aStar>=(a+b)/2:
            x1 = solve(((aStar + bStar) / 2 - x - (bStar - aStar) / 2) / (
                        x-(a + b) / 2  - (b - a) / 2 - ((bStar + aStar) / 2 - x) - (
                    bStar - aStar) / 2)-maxCorrelationNum)
            x2 = solve((x-(aStar + bStar) / 2 - (bStar - aStar) / 2) / (
                        x-(a + b) / 2 - (b - a) / 2 - (x - (bStar + aStar) / 2) - (
                    bStar - aStar) / 2)-maxCorrelationNum)
            x3 = None

            x1Num, x2Num, x3Num = self.checkData(x1[0], x2[0], x3, maxCorrelationNum, aStar, (aStar + bStar) / 2, bStar)

        else:
            if (aStar+bStar)<=(a+b):

                x1 = solve(((aStar + bStar) / 2 - x - (bStar - aStar) / 2) / (
                        (a + b) / 2 - x - (b - a) / 2 - ((bStar + aStar) / 2 - x) - (
                            bStar - aStar) / 2) - maxCorrelationNum * (bStar - aStar) / (
                                       2 * (bStar - a)))
                x2 = solve((x - (aStar + bStar) / 2 - (bStar - aStar) / 2) / (
                        (a + b) / 2 - x - (b - a) / 2 - (x - (bStar + aStar) / 2) - (
                            bStar - aStar) / 2) - maxCorrelationNum * (bStar - aStar) / (
                                       2 * (bStar - a)))
                x3 = solve((x -(aStar + bStar) / 2 - (bStar - aStar) / 2) / (
                        x - (a + b) / 2 - (b - a) / 2 - (x - (bStar + aStar) / 2) - (
                            bStar - aStar) / 2) - maxCorrelationNum * (bStar - aStar) / (
                                       2 * (bStar - a)))

                x1Num, x2Num, x3Num = self.checkData(x1[0], x2[0], x3[0], maxCorrelationNum, aStar, (aStar + bStar) / 2,(a+b)/2, bStar)

            else:
                x1 = solve(((aStar + bStar) / 2 - x - (bStar - aStar) / 2) / (
                        (a + b) / 2 - x - (b - a) / 2 - ((bStar + aStar) / 2 - x) - (
                        bStar - aStar) / 2) - maxCorrelationNum * (bStar - aStar) / (
                                   2 * (bStar - a)))
                x2 = solve(((aStar + bStar) / 2-x - (bStar - aStar) / 2) / (
                        x-(a + b) / 2 - (b - a) / 2 - ((bStar + aStar) / 2-x) - (
                        bStar - aStar) / 2) - maxCorrelationNum * (bStar - aStar) / (
                                   2 * (bStar - a)))
                x3 = solve((x -( aStar + bStar) / 2 - (bStar - aStar) / 2) / (
                        x - (a + b) / 2 - (b - a) / 2 - (x - (bStar + aStar) / 2) - (
                        bStar - aStar) / 2) - maxCorrelationNum * (bStar - aStar) / (
                                   2 * (bStar - a)))

                x1Num, x2Num, x3Num = self.checkData(x1[0], x2[0], x3[0], maxCorrelationNum, aStar, (a + b) / 2, (aStar + bStar) / 2, bStar)

        xList = []
        if x1Num is not None:
            xList.append(x1Num)
        else:
            pass
        if x2Num is not None:
            xList.append(x2Num)
        else:
            pass
        if x3Num is not None:
            xList.append(x3Num)
        else:
            pass
        if len(xList)==2:

            if jingDianYuIndexNP == 0:
                extendJingDianYuList = self.extendJingDianYu(self.jingDianYuList)
                checkTotalCorrelationNP, extendJingDianYuTuple = self.subExcuteTotalCorrelation(
                    jingDianYuList=extendJingDianYuList, evaDataList = evaDataList)
                if checkTotalCorrelationNP[0]<=checkTotalCorrelationNP[2]:
                    resScore = xList[0]
                else:
                    resScore = xList[1]
            elif jingDianYuIndexNP==len(jingDianYuTuple)-1:
                extendJingDianYuList = self.extendJingDianYu(self.jingDianYuList, direction="right")

                checkTotalCorrelationNP, extendJingDianYuTuple = self.subExcuteTotalCorrelation(
                    jingDianYuList=extendJingDianYuList, evaDataList = evaDataList)

                if checkTotalCorrelationNP[-1]<=checkTotalCorrelationNP[-3]:
                    resScore = xList[0]
                else:
                    resScore = xList[1]
            else:
                if totalCorrelationNp[jingDianYuIndexNP-1]<=totalCorrelationNp[jingDianYuIndexNP+1]:
                    resScore = xList[1]
                else:
                    resScore = xList[0]
        elif len(xList)==1:
            resScore = xList[0]
        else:
            print("计算失败")
            resScore = False

        return resScore


    def oneLayerExcute(self, evaDataList):
        totalCorrelationNP, jingDianYuTuple = self.subExcuteTotalCorrelation(jingDianYuList=self.jingDianYuList, evaDataList=evaDataList)

        jieYuTuple = self.getJieYuTuple(self.jingDianYuList)
        totalScore = self.totalScore(totalCorrelationNP,jingDianYuTuple, jieYuTuple, evaDataList)
        return totalScore

    def splitEvaData(self, dataDict, removeStringNum = 2):
        newDict = {}
        for key, valueList in dataDict.items():
            removeKey = key[0:-removeStringNum]
            if removeKey in newDict:
                if isinstance(valueList, list):
                    newDict[removeKey].append(float(valueList[-1]))
                else:
                    newDict[removeKey].append(float(valueList))
            else:
                if isinstance(valueList, list):
                    newDict[removeKey] = [float(valueList[-1])]
                else:
                    newDict[removeKey] = [float(valueList)]
        return newDict


    def oneLayerMultiExcute(self, newDict):


        scoreTuple = tuple(tuple((key, self.oneLayerExcute(evaDataList=valueList))) \
                               if len(valueList)>1 else tuple((key,valueList[0])) \
                           for key,valueList in newDict.items())

        scoreDict = dict(scoreTuple)
        return scoreDict


    def addresDict(self):
        dataJson = json.loads(self.dataJson)

        valuesLi = []
        for key, valueList in dataJson.items():

            valueList.append(key)
            valuesLi.append(valueList)
        evaDF = pd.DataFrame(valuesLi, columns = ["评价阶段名称", "评价者名称", "一级评价指标名称", "二级评价指标名称", "二级评价指标量值", "二级评价指标编码"])
        evaDF["一级评价指标编码"] = evaDF["二级评价指标编码"].map(lambda x:x[:-2])
        evaDF["评价者编码"] = evaDF["一级评价指标编码"].map(lambda x:x[:-2])
        evaDF["评价阶段编码"] = evaDF["评价者编码"].map(lambda x:x[:-1])
        seniorResDF = evaDF.drop(columns=["二级评价指标名称", "二级评价指标编码", "二级评价指标量值"])
        seniorResDF.drop_duplicates(subset=["一级评价指标编码"], inplace=True)
        seniorScoreDict, evaluatorScoreDict, peroidScoreDict, totalScoreDict = self.excute()

        seniorResDF["一级评价指标结果"] = seniorResDF["一级评价指标编码"].map(seniorScoreDict)

        evaluatorResDF = seniorResDF.drop(columns=["一级评价指标编码","一级评价指标结果", "一级评价指标名称"])
        evaluatorResDF.drop_duplicates(subset=["评价者编码"],inplace=True)
        evaluatorResDF["评价者结果"] = evaluatorResDF["评价者编码"].map(evaluatorScoreDict)

        periodResDF = evaluatorResDF.drop(columns=["评价者编码", "评价者结果", "评价者名称"])
        periodResDF.drop_duplicates(subset=["评价阶段编码"], inplace=True)
        periodResDF["评价阶段结果"] = periodResDF["评价阶段编码"].map(peroidScoreDict)

        return evaDF, seniorResDF,evaluatorResDF,periodResDF,totalScoreDict


    def excute(self):
        dataJson = json.loads(self.dataJson)
        juniorIndexDict = self.splitEvaData(dataJson)

        seniorScoreDict = self.oneLayerMultiExcute(juniorIndexDict)

        seniorIndexDict = self.splitEvaData(seniorScoreDict)
        evaluatorScoreDict = self.oneLayerMultiExcute(seniorIndexDict)

        evaluatorIndexDict = self.splitEvaData(evaluatorScoreDict,removeStringNum=1)
        peroidScoreDict = self.oneLayerMultiExcute(evaluatorIndexDict)

        totalData = {"t":list(peroidScoreDict.values())}
        totalScoreDict = self.oneLayerMultiExcute(totalData)

        return seniorScoreDict, evaluatorScoreDict,peroidScoreDict,totalScoreDict

if __name__ == "__main__":
    obj = ExtAssMethod(
        dataJson="""{"100931": ["\u8bd5\u7528", "\u7ba1\u7406\u8005", "\u6295\u8d44\u56de\u62a5\u9884\u8ba1", "\u5e93\u5b58\u8d44\u91d1\u5360\u7528\u7387", "3"], "101033": ["\u8bd5\u7528", "\u7ba1\u7406\u8005", "\u8d44\u6e90\u5229\u7528", "\u7f51\u7edc\u6027\u80fd\u63d0\u9ad8\u7387", "5"], "101034": ["\u8bd5\u7528", "\u7ba1\u7406\u8005", "\u8d44\u6e90\u5229\u7528", "\u8ba1\u7b97\u673a\u62e5\u6709\u63d0\u9ad8\u7387", "6"], "101136": ["\u8bd5\u7528", "\u7ba1\u7406\u8005", "\u73b0\u72b6\u6539\u53d8", "\u7ec4\u7ec7\u7ed3\u6784\u7684\u4f18\u5316", "8"], "101138": ["\u8bd5\u7528", "\u7ba1\u7406\u8005", "\u73b0\u72b6\u6539\u53d8", "\u4e1a\u52a1\u6d41\u7a0b\u7684\u6539\u5584", "7"], "111343": ["\u8bd5\u7528", "\u5185\u63a7\u8005", "\u9879\u76ee\u8fdb\u5ea6", "\u5728\u7ebf\u7528\u6237\u7387", "8"], "111345": ["\u8bd5\u7528", "\u5185\u63a7\u8005", "\u9879\u76ee\u8fdb\u5ea6", "\u5458\u5de5\u57f9\u8bad\u5408\u683c\u7387", "7"], "121448": ["\u8bd5\u7528", "\u4f7f\u7528\u8005", "\u8bd5\u7528\u9002\u5e94\u5ea6", "\u4e1a\u52a1\u8986\u76d6\u5ea6", "7"], "201551": ["\u79df\u7528", "\u7ba1\u7406\u8005", "\u76f4\u63a5\u7ecf\u6d4e\u6548\u76ca", "\u9500\u552e\u989d\u589e\u957f\u7387", "8"], "201553": ["\u79df\u7528", "\u7ba1\u7406\u8005", "\u76f4\u63a5\u7ecf\u6d4e\u6548\u76ca", "\u8282\u7ea6\u7684\u6210\u672c", "8"], "201654": ["\u79df\u7528", "\u7ba1\u7406\u8005", "\u95f4\u63a5\u7ecf\u6d4e\u6548\u76ca", "\u8fde\u5e26\u6548\u76ca", "9"], "201758": ["\u79df\u7528", "\u7ba1\u7406\u8005", "\u793e\u4f1a\u6548\u76ca", "\u793e\u4f1a\u5f71\u54cd\u5ea6", "6"], "211962": ["\u79df\u7528", "\u5185\u63a7\u8005", "\u76ee\u6807\u5b9e\u73b0", "\u5458\u5de5\u638c\u63e1\u5ea6", "7"], "211963": ["\u79df\u7528", "\u5185\u63a7\u8005", "\u76ee\u6807\u5b9e\u73b0", "\u6a21\u5757\u529f\u80fd\u4f7f\u7528\u5ea6", "8"], "000000": ["\u9009\u578b", "\u7ba1\u7406\u8005", "\u4f01\u4e1a\u6218\u7565", "\u4f01\u4e1a\u6218\u7565\u4e00\u81f4\u6027", "8"], "000207": ["\u9009\u578b", "\u7ba1\u7406\u8005", "\u8f6f\u786c\u4ef6\u57fa\u7840\u80fd\u529b", "\u8ba1\u7b97\u673a\u8054\u7f51\u7387", "8"], "000209": ["\u9009\u578b", "\u7ba1\u7406\u8005", "\u8f6f\u786c\u4ef6\u57fa\u7840\u80fd\u529b", "\u529e\u516c\u81ea\u52a8\u5316\u6c34\u5e73", "6"], "010414": ["\u9009\u578b", "\u5185\u63a7\u8005", "\u670d\u52a1\u54cd\u5e94", "\u95ee\u9898\u54cd\u5e94\u5ea6", "6"], "010416": ["\u9009\u578b", "\u5185\u63a7\u8005", "\u670d\u52a1\u54cd\u5e94", "\u54cd\u5e94\u53ca\u65f6\u5ea6", "6"], "010517": ["\u9009\u578b", "\u5185\u63a7\u8005", "\u4e91\u670d\u52a1\u5546\u8d28\u91cf", "\u5e02\u573a\u4efd\u989d", "5"], "010520": ["\u9009\u578b", "\u5185\u63a7\u8005", "\u4e91\u670d\u52a1\u5546\u8d28\u91cf", "\u7528\u6237\u4f7f\u7528\u5e74\u9650", "4"], "010625": ["\u9009\u578b", "\u5185\u63a7\u8005", "\u7cfb\u7edf\u529f\u80fd", "\u4e91\u7aef\u7cfb\u7edf\u6587\u6863\u5b8c\u5907\u6027", "5"], "020727": ["\u9009\u578b", "\u4f7f\u7528\u8005", "\u63a5\u53d7\u5ea6", "\u4e0e\u7ec4\u7ec7\u7ed3\u6784\u7684\u7ed3\u5408\u5ea6", "6"], "020729": ["\u9009\u578b", "\u4f7f\u7528\u8005", "\u63a5\u53d7\u5ea6", "\u4e0e\u7528\u6237\u9700\u6c42\u7684\u5339\u914d\u5ea6", "9"]}""",
        jingDianYuList=[0, 2, 4, 6, 8, 10])

    obj.addresDict()
