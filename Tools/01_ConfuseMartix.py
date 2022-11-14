
class ConfuseMartix():
    def __init__(self, martix):
        self.martix = martix

    '''
    总体准确率
    '''
    def accuracy(self):
        count = 0
        sum_ = 0
        for i in range(len(self.martix)):
            count += self.martix[i][i]
            sum_ += sum(self.martix[i])
        return count / sum_

    '''
    每类的精确度
    '''
    def precision(self):
        precision = []
        for i in range(len(x)):
            count = 0
            for j in range(len(x)):
                count += x[j][i]
            pre = x[i][i] / count
            precision.append(pre)
        return precision

    '''
    每类的召回率
    '''
    def recall(self):
        recall = []
        for i in range(len(x)):
            count = 0
            for j in range(len(x)):
                count += x[i][j]
            rec = x[i][i] / count
            recall.append(rec)
        return recall

    '''
    每类的f1_score
    '''
    def f1score(self):
        f1_score = []
        for i in range(len(self.martix)):
            score = (2 * self.precision()[i] * self.recall()[i]) / (self.precision()[i] + self.recall()[i])
            f1_score.append(score)
        return f1_score


# 横坐标为模型猜测结果，纵坐标为真实标签

# 测试案例

# x = [[470,64,2,5],
#      [24,600,14,24],
#      [5,12,620,11],
#      [5,19,53,580]]

# c = ConfuseMartix(x)
# print(c.accuracy())
# print(c.precision())
# print(c.recall())
# print(c.f1score())
