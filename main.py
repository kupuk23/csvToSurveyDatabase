# This is a sample Python script.
import csv
import facet_ss as FacetRules
import dom_func as DomainRules
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("ServiceAccount.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

dummy = ['0', '1', '2', '3', '4', '5']
nik = []
facet1 = []
facet2 = []
facet3 = []
facet4 = []
facet5 = []
facet6 = []
facet7 = []
facet8 = []
facet9 = []
facet10 = []
facet11 = []
facet12 = []
facet13 = []
facet14 = []
facet15 = []
dom1 = []  # Agreeableness -- Faset 1,2,3
dom2 = []  # Conscientiousness -- Faset 4,5,6
dom3 = []  # Emotional Stability -- Faset 7,8,9
dom4 = []  # Extraversion -- Faset 10,11,12
dom5 = []  # Open Mindedness -- Faset 13,14,15


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settin`gs.`
def getCSV():
    with open('datautf.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        next(csv_reader)
        for data in csv_reader:
            nik.append(data[0])
            intData = [int(stringData) for stringData in data]
            cnt = 0

            for num in range(1, 61, 4):

                summedItem = 0
                for item in intData[num:num + 4]:
                    summedItem += item
                cnt += 1
                add_facet(cnt, summedItem)


def add_facet(cnt, summedItem):
    if cnt == 1:
        facet1.append(summedItem)
    elif cnt == 2:
        facet2.append(summedItem)
    elif cnt == 3:
        facet3.append(summedItem)
    elif cnt == 4:
        facet4.append(summedItem)
    elif cnt == 5:
        facet5.append(summedItem)
    elif cnt == 6:
        facet6.append(summedItem)
    elif cnt == 7:
        facet7.append(summedItem)
    elif cnt == 8:
        facet8.append(summedItem)
    elif cnt == 9:
        facet9.append(summedItem)
    elif cnt == 10:
        facet10.append(summedItem)
    elif cnt == 11:
        facet11.append(summedItem)
    elif cnt == 12:
        facet12.append(summedItem)
    elif cnt == 13:
        facet13.append(summedItem)
    elif cnt == 14:
        facet14.append(summedItem)
    elif cnt == 15:
        facet15.append(summedItem)


def calc_dom():
    for data in range(0, len(nik)):
        dom1.append(facet1[data] + facet2[data] + facet3[data])
        dom2.append(facet4[data] + facet5[data] + facet6[data])
        dom3.append(facet7[data] + facet8[data] + facet9[data])
        dom4.append(facet10[data] + facet11[data] + facet12[data])
        dom5.append(facet13[data] + facet14[data] + facet15[data])


def convert_facet():
    for data in range(0, len(nik)):
        FacetRules.facet1_toSS(facet1, data)
        FacetRules.facet2_toSS(facet2, data)
        FacetRules.facet3_toSS(facet3, data)
        FacetRules.facet4_toSS(facet4, data)
        FacetRules.facet5_toSS(facet5, data)
        FacetRules.facet6_toSS(facet6, data)
        FacetRules.facet7_toSS(facet7, data)
        FacetRules.facet8_toSS(facet8, data)
        FacetRules.facet9_toSS(facet9, data)
        FacetRules.facet10_toSS(facet10, data)
        FacetRules.facet11_toSS(facet11, data)
        FacetRules.facet12_toSS(facet12, data)
        FacetRules.facet13_toSS(facet13, data)
        FacetRules.facet14_toSS(facet14, data)
        FacetRules.facet15_toSS(facet15, data)


def convert_domain():
    for data in range(0, len(nik)):
        DomainRules.dom1_toSS(dom1, data)
        DomainRules.dom2_toSS(dom2, data)
        DomainRules.dom3_toSS(dom3, data)
        DomainRules.dom4_toSS(dom4, data)
        DomainRules.dom5_toSS(dom5, data)


def upload_data():
    done = 0
    for data in range(0, len(nik)):
        db.collection('userCSV2').add(
            {
                'nik': nik[data],
                'facet1': facet1[data],
                'facet2': facet2[data],
                'facet3': facet3[data],
                'facet4': facet4[data],
                'facet5': facet5[data],
                'facet6': facet6[data],
                'facet7': facet7[data],
                'facet8': facet8[data],
                'facet9': facet9[data],
                'facet10': facet10[data],
                'facet11': facet11[data],
                'facet12': facet12[data],
                'facet13': facet13[data],
                'facet14': facet14[data],
                'facet15': facet15[data],
                'dom1': dom1[data],
                'dom2': dom2[data],
                'dom3': dom3[data],
                'dom4': dom4[data],
                'dom5': dom5[data],
            }
        )
        done += 1
        print('{} of {} Uploaded.'.format(done,len(nik)))


if __name__ == '__main__':
    getCSV()
    calc_dom()
    convert_facet()
    convert_domain()
    upload_data()
    # print ('{} \n'.format(nik))
    # print('{} \n'.format(dom1))
    # print('{} \n'.format(dom2))
    # print('{} \n'.format(dom3))
    # print('{} \n'.format(dom4))
    # print('{} \n'.format(dom5))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
