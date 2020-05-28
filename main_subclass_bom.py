# -*- coding: utf-8 -*-
"""
Created by Dufy on 2019/12/2  11:00
IDE used: PyCharm
Description :
1)增加所有模型的预测效果
2)
Remark:
"""
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
import time
import fasttext as ff
# # from fastText.bui
# from fastText.build import fasttext as ff
from sklearn.metrics import confusion_matrix
from sklearn import metrics
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
from data_operation.function import get_logger
from bom_read import excel_read2txt
from data_selection_new import mergeLabelTxt
from data_split import datasSplit
import pandas as pd
from data_operation import OperateExcel
import time
from data_operation.function import load_stop_word_list, standard, labelNewSubclass, path_clear
from data_operation.txt_operate import OperateTXT
import os
import numpy as np
np.set_printoptions(threshold=np.inf)
from data_operation.constant import label_name_forbid
stop_words = load_stop_word_list("stopwords_subclass.txt")


class FastTextModel:
    def __init__(self, epoch, loss, learn_rate):
        '''
        初始化网络，设置损失函数，迭代数///
        '''
        self.epoch = epoch
        self.loss = loss
        self.lr = learn_rate
        self.n_gram = 2
        pass

    def train(self, train_file_path):
        '''
        依据训练数据不断更新权重
        '''
        for i in range(1, self.epoch):  # 迭代轮数
            w = self.n_gram
            start_time = time.time()  # loss = softmax or hs
            classifier = ff.train_supervised(train_file_path,
                                             epoch=i,
                                             loss=self.loss,
                                             lr=self.lr,
                                             dim=35,
                                             wordNgrams=w,
                                             minCount=1,  # 词频阈值, 小于该值在初始化时会过滤掉
                                             minn=3,
                                             maxn=15)
            print("ngram=%d,训练第%d轮，用时%s" % (w, i, time.time() - start_time))
            classifier.save_model(r"D:\dufy\code\local\model\ft_subclass\model_w" + str(w) + "_e" + str(i))
            print('============训练进度{:.2}============='.format((i - 1)/(self.epoch - 2)))
        print('训练完成......')

    def evaluate1(self, train_file_path, test_file_path):
        '''
        调参
        :return:
        '''
        plot_x_epoch = list(range(2, self.epoch))
        # 加载测试数据
        correct_labels = []
        texts = []
        test_accuracy = []
        train_accuracy = []
        test_f1 = []
        with open(test_file_path, "r", encoding="utf-8") as ft_test:
            for line in ft_test:
                # print(line)
                correct_labels.append(line.strip().split(" , ")[0])
                texts.append(line.strip().split(" , ")[1])
        # print('correct_labels 为：{}'.format(correct_labels))
        # 加载分类模型
        #for w in range(1, 2):
        for i in range(2, self.epoch):
            w = self.n_gram
            classifier = ff.load_model(r"D:\dufy\code\ft_BOM\model\model_w" + str(w) + "_e" + str(i))
            # print("Model/model_w" + str(w) + "_e" + str(i))
            # 预测
            # classifier.get_word_vector()
            predict_labels = classifier.predict(texts)[0]
            # print(dir(classifier),';;;;;;;')
            # print('测试集predict_labels 为：', predict_labels, type(predict_labels))
            print(confusion_matrix(correct_labels, predict_labels,
                                   labels=label_list))
            f1_score = metrics.f1_score(correct_labels, predict_labels,
                                        average='weighted')
            print('\033[1;32m 测试集F1: {:.3}\033[0m'.format(f1_score))
            test_f1.append(f1_score)
            # 计算预测结果
            # print(len(texts))
            accuracy_num = 0
            for j in range(len(texts)):
                if predict_labels[j][0] == correct_labels[j]:
                    # print(predict_labels[j][0], correct_labels[j], '===~~~~~~~')
                    accuracy_num += 1

            accuracy = accuracy_num / len(texts)
            test_accuracy.append(accuracy)
            # print("正确率：%s" % accuracy)
            print('Model/model_w{}_e{}正确率：{:.2}'.format(w, i, accuracy))
            print('=====分隔符======')
        print(test_accuracy, test_f1)  # 包括了n1, 和n2
        test_accuracy_n1 = test_accuracy
        # test_accuracy_n2 = test_accuracy[(epoch_ - epoch_begin):]
        test_f1_n1 = test_f1
        # test_f1_n2 = test_f1[(epoch_ - epoch_begin):]
        # ====================训练数据==================
        print('计算训练数据......')
        correct_labels_train = []
        texts1 = []

        with open(train_file_path, "r", encoding="utf-8") as ft_train:
            for line in ft_train:
                # print(line, '--------------------')
                # print(line.strip().split(" , ")[0], '--------------------')
                try:
                    correct_labels_train.append(line.strip().split(" , ")[0])
                    texts1.append(line.strip().split(" , ")[1])
                except:
                    continue
        # print('correct_labels 为：{}'.format(correct_labels_train))
        # 加载分类模型

        for i in range(2, self.epoch):
            w = self.n_gram
            classifier = ff.load_model(r"D:\dufy\code\ft_BOM\model\model_w" + str(w) + "_e" + str(i))
            # print("Model/model_w" + str(w) + "_e" + str(i))
            # 预测
            predict_labels = classifier.predict(texts1)[0]
            # print(predict_labels,'--------------------')
            # 计算预测结果
            # print(len(texts))
            accuracy_num = 0
            for j in range(len(texts1)):
                if predict_labels[j][0] == correct_labels_train[j]:
                    accuracy_num += 1
            # print(accuracy_num,'--------------------')
            accuracy = accuracy_num / len(texts1)
            train_accuracy.append(accuracy)
            # print("训练集正确率：%s" % accuracy)
            print('训练集Model/model_w{}_e{}正确率：{:.2}'.format(w, i, accuracy))

        train_accuracy_n1 = train_accuracy
        # train_accuracy_n2 = train_accuracy[(epoch_ - epoch_begin):]
        plt.figure()
        plt.plot(plot_x_epoch, test_accuracy_n1, color="r", linestyle="-", marker="^", linewidth=1,
                 label="validation_accu")
        plt.plot(plot_x_epoch, test_f1_n1, color="b", linestyle="-", marker="o", linewidth=1, label="validation_f1")
        plt.plot(plot_x_epoch, train_accuracy_n1, color="k", linestyle="-", marker="s", linewidth=1, label="train_accu")
        # plt.legend(loc='upper left', bbox_to_anchor=(0.1, 0.95))
        plt.xlabel("epoch")
        plt.ylabel("accuracy")
        plt.legend()
        plt.title("{}-gram".format(w))
        plt.grid()
        time_temp = time.strftime("(T%Y-%m-%d-%H-%M)", time.localtime())
        plt.savefig(r"D:\dufy\code\fast_subclass30\pic\{}.png".format(time_temp+"rate" + str(self.lr) + '_'+str(w)+'-gram_' + self.loss))
        plt.show()
        logger.info('训练结束...')

    @staticmethod
    def loadTrainData(file_path):
        """ 加载 BOM标注数据路径
        :return:标签和样本描述
        """
        pass
        correct_labels = []
        texts_content = []
        with open(file_path, "r", encoding="utf-8") as ft_test:
            for line in ft_test:
                correct_labels.append(line.strip().split(" , ")[0].replace('__label__',''))
                texts_content.append(line.strip().split(" , ")[1])
        return correct_labels, texts_content

    def evaluate(self, classifier_model, file_path):
        """
        评价模型效果
        :param classifier_model: 单个分类模型
        :param file_path:  Bom标注数据路径
        :return:
        """
        vali_correct_labels, vali_texts = self.loadTrainData(file_path)

        # print(f'验证集标签：{vali_correct_labels}')
        predict_labels = []
        model_predict_labels = classifier_model.predict(vali_texts)[0]
        for i in model_predict_labels:
            predict_labels.append(i[0].replace('__label__', ''))
        # print(f'验证集预测标签：{vali_predict_labels}')
        # print(f'准确率计算：{accuracy_score(vali_correct_labels, vali_predict_labels)}')
        # print(f"f1宏平均：{metrics.f1_score(vali_correct_labels, vali_predict_labels, average='macro')}" )

        logger.debug(f'标签：{label_list}')
        labels_ = []
        for i in label_list:
            labels_.append(i.replace('__label__',''))
        logger.debug(confusion_matrix(vali_correct_labels, predict_labels,labels=labels_))

        confusion_matrix_model_i = confusion_matrix(vali_correct_labels, predict_labels,labels=labels_)

        logger.debug(f'混淆矩阵：{confusion_matrix_model_i}')  # 横为预测，  竖为真实

        logger.debug('分类报告:')
        logger.debug(classification_report(vali_correct_labels, predict_labels, target_names=labels_))

        return accuracy_score(vali_correct_labels, predict_labels), metrics.f1_score(vali_correct_labels, predict_labels, average='macro')

def predict_output(str1, model):
    print('前3预测： ', model.predict([str1], k=3))
    predict = model.predict([str1])
    return predict


class TestExcel(OperateExcel):  # 重写函数

    def __init__(self, url):
        OperateExcel.__init__(self, url)

    def predict_result(self, model): # 处理单个文件
        true_false_list = []
        probability_list = []

        _, row = self.excel_matrix() # 读取列
        row = list(range(1, row))
        if row:
            j = 0
            for line_read in self.excel_content_all().splitlines():  # 先遍历行
                j += 1
                true_label = line_read.split()[0].replace('/', '')  # 替换标签里面 '/'
                if true_label in label_name_forbid:
                    continue
                true_label = labelNewSubclass(true_label)

                if true_label != 'nan':
                    print('#{}{}:'.format(j, true_label))
                    aa_description = " ".join(line_read.split()[1:])
                    aa_description_standard = standard(aa_description, stop_words)  # 标准化处理
                    predicted_result = predict_output(aa_description_standard, model)
                else:
                    continue

                predicted_label = predicted_result[0][0][0].replace('__label__', '')
                predicted_probability = predicted_result[1][0][0]
                print(predicted_probability, '!!!!!!')
                probability_list.append(predicted_probability)
                if true_label == predicted_label:
                    true_false_list.append(1)
                    print("预测实体为：\033[1;32m {} {}\033[0m".format(predicted_label, '√'))

                else:
                    print('\033[1;31m error!!【{}】\033[0m预测为\033[1;31m 【{}】\033[0m]'.format(
                        true_label, predicted_label))
                    print(self.file_path)
                    error_info = true_label + '     预测为     ' + predicted_label + ' '*10 + '概率:' + \
                                 str(predicted_probability) + f'    \Bom片段：【{aa_description_standard[:10]}】 ' + \
                                 str(self.file_path).replace(excel_path, '') + \
                                 f'{model.predict([aa_description_standard], k=3)}'.replace('__label__', '')
                    save_test_info(error_info, true_label, aa_description_standard, aa_description, predicted_probability)
                    true_false_list.append(0)
                    print("预测实体为：\033[1;31m {} {}\033[0m".format(predicted_label, '×'))
                print('========================')
            return true_false_list, probability_list
        else:
            return None, None


def save_test_info(error_info, true_label, aa_description_standard, aa_description, predicted_probability):
    pass
    OperateTXT().txt_write_line(r'D:\dufy\code\fast_subclass30\test\aaa.txt', error_info)
    OperateTXT().txt_write_line(r'D:\dufy\code\fast_subclass30\test\bbb.txt',
                                '__label__' + true_label + ' , ' + aa_description_standard)
    OperateTXT().txt_write_line(r'D:\dufy\code\fast_subclass30\test\ccc.txt',
                                '__label__' + true_label + ' , ' + aa_description)
    if predicted_probability > 0.6:
        OperateTXT().txt_write_line(r'D:\dufy\code\fast_subclass30\test\error_0.6.txt', error_info + '\n'
                                    +'__label__' + true_label + ' , '+aa_description+ '\n'
                                    +'======' )


if __name__ == '__main__':
    logger = get_logger()

    excel_read_tag = 10
    if excel_read_tag == 1:
        excel_read2txt()

    train_tag = 1
    if train_tag == 1:
        # 2 读取上一步不同txt 融合，写入'selection_data.txt'
        label_list = mergeLabelTxt(1500000, shuffle_tag=1)  ## 选取行数

        # # # 3 划分数据集
        # datasSplit()
        # 读取误分类数据到训练集
        # with open(r'.\data\error_record.txt', 'r', encoding='utf-8') as file:
        #     for line in file.readlines():
        #         OperateTXT().txt_write_line(r'.\data\corpus\train_data.txt', line.replace('\n', ''))

        # 4 训练-调参
        epoch_begin = 2
        epoch_ = 5  # 100
        loss_name = 'softmax'
        learn_rate = 0.5  # 0.5, 0.8

        ft_ = FastTextModel(epoch_, loss_name, learn_rate)
        # ft_.train(r'.\data\corpus\train_data.txt')  # 训练
        # ft_.evaluate(r'.\data\corpus\train_data.txt', r'.\data\corpus\vali_data.txt')   #

        # 记录
        train_accuracy_list = []  # 准确率
        train_f1_macro_list = []  # f1 宏平均
        val_accuracy_list = []
        val_f1_macro_list = []

        for i in range(1, epoch_):
            pass
            w = ft_.n_gram
            classifier_model_i = ff.load_model(r"D:\dufy\code\local\model\ft_subclass\model_w" + str(w) + "_e" + str(i))
            logger.debug('============')
            logger.debug(f'epoch_{i}, 训练集: ')
            accuarcy, f1_score = ft_.evaluate(classifier_model_i, r'.\data\corpus\train_data.txt')
            train_accuracy_list.append(accuarcy)
            train_f1_macro_list.append(f1_score)

            logger.debug('============')
            logger.debug(f'epoch_{i}, 验证集: ')
            accuarcy, f1_score = ft_.evaluate(classifier_model_i, r'.\data\corpus\vali_data.txt')
            val_accuracy_list.append(accuarcy)
            val_f1_macro_list.append(f1_score)

        print(f'训练集准确率：{train_accuracy_list}')
        print(f'训练集f1：{train_f1_macro_list}')
        print(f'验证集准确率：{val_accuracy_list}')
        print(f'验证集f1：{val_f1_macro_list}')

        plot_x = list(range(1, epoch_))
        plt.figure()
        plt.plot(plot_x, train_accuracy_list, color="k", linestyle="-", marker="^", linewidth=1, label="train_accu")
        plt.plot(plot_x, train_f1_macro_list, color="k", linestyle="-", marker="X", linewidth=1, label="train_f1")
        plt.plot(plot_x, val_accuracy_list, color="r", linestyle="-", marker="^", linewidth=1, label="val_accu")
        plt.plot(plot_x, val_f1_macro_list, color="r", linestyle="-", marker="X", linewidth=1, label="val_f1")
        # plt.legend(loc='upper left', bbox_to_anchor=(0.1, 0.95))
        plt.xlabel("epoch", fontsize=20)
        plt.ylabel("property", fontsize=20)
        plt.legend()
        # plt.title("{}-gram".format(w))
        plt.grid()
        # time_temp = time.strftime("(T%Y-%m-%d-%H-%M)", time.localtime())
        time_temp = time.strftime("(T%Y-%m-%d-%H)", time.localtime())
        plt.savefig(r".\pic\{}.png".format(time_temp + "rate" + str(ft_.lr) + '_' + str(w) + '-gram_' + ft_.loss))
        plt.show()



    # 5 测试
    test_flag = 1

    if test_flag == 1:
        excel_path = r'C:\Users\Administrator\Documents\Tencent Files\3007490756\FileRecv\test00'
        excel_path = r'C:\Users\Administrator\Documents\Tencent Files\3007490756\FileRecv\5.22Mike'

        model_folder = r'D:\dufy\code\ft_BOM\model_1'  # 单个模型测试
        model_names = os.listdir(model_folder)

        dict_model_test = {}
        record_right_probability_list = []
        record_wrong_probability_list = []

        for i, name0 in enumerate(model_names):  # 文件夹下文件循环
            modle_path = model_folder + '\\' + name0
            prediciton_model = ff.load_model(modle_path)
            path_clear(r'D:\dufy\code\fast_subclass30\test')

            all_record = 0
            right_record = 0

            file_names = os.listdir(excel_path)
            for i, name1 in enumerate(file_names):
                file_path_combine = excel_path + '\\' + name1
                aa = TestExcel(file_path_combine)

                TF_record, probability_record = aa.predict_result(prediciton_model)  # 预测 excel 一行,除去标签
                if probability_record:
                    for index, value in enumerate(TF_record):
                        if value:
                            record_right_probability_list.append(probability_record[index])
                        else:
                            record_wrong_probability_list.append(probability_record[index])

                if TF_record:
                    print('正确率:{:.2f}'.format(sum(TF_record) / len(TF_record)))
                    all_record += len(TF_record)
                    for i in TF_record:
                        if i == 1:
                            right_record += 1
                else:
                    print('{} 无法识别'.format(file_path_combine))
                    logger.info(f'有问题的excel；{file_path_combine}')
                print(file_path_combine)
                print('\033[1;32m =\033[0m' * 120)
                pass
            print('标注数据量:{}'.format(all_record))
            print('预测正确量:{}'.format(right_record))
            print('测试集全部数据正确率:{:.2f}'.format(right_record / all_record))
            print('全部结束！！！！')
            dict_model_test[name0] = right_record / all_record  # 此处。。。。
        print(dict_model_test)

        plt.scatter(list(range(len(record_wrong_probability_list))), record_wrong_probability_list, color="r",
                    marker="x", linewidth=1, label="wrong label")
        plt.scatter(list(range(len(record_right_probability_list))), record_right_probability_list, color="b",
                    marker="o", linewidth=1, label="right label")
        plt.grid()
        plt.xlabel("Sample Number")
        plt.ylabel("Probability")
        plt.legend(loc='lower right')
        plt.show()

        x = []
        y = []
        for key, value in dict_model_test.items():
            print(value)
            x.append(key.strip('model_'))  # append() 方法用于在列表末尾添加新的对象。
            y.append(value)

        plt.plot(x, y, "b-o", linewidth=2)
        plt.xlabel("model")  # X轴标签
        plt.ylabel("accu")  # Y轴标签
        plt.title("Line plot")  # 图标题
        plt.grid()
        plt.show()  # 显示图

    if test_flag == 0:
        ft_vec = ff.load_model(r"D:\dufy\code\ft_BOM\model\model_w2_e98")
        print(ft_vec.get_word_vector('3v'))
        print(ft_vec.words)
        print(ft_vec.get_nearest_neighbors('3v'))
        print(ft_vec.get_nearest_neighbors('0402B104K160CT'.lower()))
        print(ft_vec.get_nearest_neighbors('0402B104K160Cj'.lower()))
        print(ft_vec.get_nearest_neighbors('50v-0402B104K160-xxxxxxx'.lower()))
        print(ft_vec.get_nearest_neighbors('50 v'.lower()))
        print(ft_vec.get_nearest_neighbors('50v'.lower()))
        print(ft_vec.get_nearest_neighbors('MCS0630-3R3MN2'.lower()))
        print(ft_vec.get_nearest_neighbors('AOD510'.lower()))
        print(ft_vec.get_nearest_neighbors('电器'.lower()))
        print(ft_vec.get_nearest_neighbors('MCS0630-3R3MN2'.lower()))
    # aa = ['v', 'p2sd0301000026']
    # for i in aa:
    #     print(classifier.get_word_vector(i),'=======')
    #
    # print(dir(classifier))
    # print(help(classifier.ge))



