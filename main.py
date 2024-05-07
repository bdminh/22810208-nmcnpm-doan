from tabulate import tabulate
import os

from Controller.Home import controller

if __name__ == '__main__':
    while(True):
        print('''
                ################## Danh sách các chức năng ##################    
                                            
                1. Xem dữ liệu CCF
                2. Xem dữ liệu LIX Ahead Conference
                3. Xem dữ liệu LIX Future Conference
                4. Xem dữ liệu LIX Planning Conference
                5. Xem dữ liệu LIX Running Conference
                6. Tra cứu tên đầy đủ qua ID Conference
                7. Tìm kiếm thông tin hội nghị (ID Conference, city, deadline)
                8. Cập nhật dữ liệu từ CCF 
                9. Cập nhật dữ liệu từ LIX, Ecole Polytechnique
                10. Xuất Excel CCF
                11. Xuất Excel LIX Ahead Conference
                12. Xuất Excel LIX Future Conference
                13. Xuất Excel LIX Planning Conference
                14. Xuất Excel LIX Running Conference
                15. Thoát
                
                ''')
        
        n=input('Vui lòng nhập lựa chọn (1 - 15): ')

        choice=int(n)
        if choice==1:
            table=controller.getDataCCF()
            print(tabulate(table))
            print("Nhấn enter để tiếp tục: ")
            temp=input()
            returned_value = os.system('clear')
        elif choice==2:
            table=controller.getDataLixAhead()
            print(tabulate(table))
            print("Nhấn enter để tiếp tục: ")
            temp=input()
            returned_value = os.system('clear')
        elif choice==3:
            table=controller.getDataLixFuture()
            print(tabulate(table))
            print("Nhấn enter để tiếp tục: ")
            temp=input()
            returned_value = os.system('clear')
        elif choice==4:
            table=controller.getDataLixPlanning()
            print(tabulate(table))
            print("Nhấn enter để tiếp tục: ")
            temp=input()
            returned_value = os.system('clear')
        elif choice==5:
            table=controller.getDataLixRunning()
            print(tabulate(table))
            print("Nhấn enter để tiếp tục: ")
            temp=input()
            returned_value = os.system('clear')
        elif choice==6:
            break
        elif choice==7:
            break
        elif choice==8:
            result=controller.updateDataCCF()
            print(result)
            print("Nhấn enter để tiếp tục: ")
            temp=input()
            returned_value = os.system('clear')
        elif choice==9:
            result=controller.updateDataLix()
            print(result)
            print("Nhấn enter để tiếp tục: ")
            temp=input()
            returned_value = os.system('clear')
        elif choice==10:
            result=controller.exportDataCCF()
            print(result)
        elif choice==11:
            result=controller.exportDataLixAhead()
            print(result)
        elif choice==12:
            result=controller.exportDataLixFuture()
            print(result)
        elif choice==13:
            result=controller.exportDataLixPlanning()
            print(result)
        elif choice==14:
            result=controller.exportDataLixRunning()
            print(result)
        elif choice==15:
            break
        else:
            print("Nhập sai lựa chọn! lựa chọn đúng từ 1 đến 15")

# from tabulate import tabulate
# table = [['col 1', 'col 2', 'col 3', 'col 4'], [1, 2222, 30, 500], [4, 55, 6777, 1]]
# print(tabulate(table))