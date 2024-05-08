from tabulate import tabulate
import os

from Controller.Home import controller

if __name__ == '__main__':
    path=os.path.dirname(os.path.abspath(__file__))
    if os.path.isfile(f'{path}\\Models\\qldh.sqlite') is False:
        print("Không thể kết nối cơ sở dữ liệu, xin thử lại sau")
        temp=input()
        quit()
    
    while(True):
        print('''
                ################## Danh sách các chức năng ##################

                1. Xem dữ liệu CCF
                2. Xem dữ liệu LIX Ahead Conference
                3. Xem dữ liệu LIX Future Conference
                4. Xem dữ liệu LIX Planning Conference
                5. Xem dữ liệu LIX Running Conference
                6. Tra cứu tên đầy đủ qua ID Conference
                7. Tìm kiếm thông tin hội nghị 
                8. Cập nhật dữ liệu từ CCF 
                9. Cập nhật dữ liệu từ LIX, Ecole Polytechnique
                10. Xuất Excel CCF
                11. Xuất Excel LIX Ahead Conference
                12. Xuất Excel LIX Future Conference
                13. Xuất Excel LIX Planning Conference
                14. Xuất Excel LIX Running Conference
                15. Thoát
                
                #############################################################
                ''')
        
        n=input('Vui lòng nhập lựa chọn (1 - 15): ')

        choice=int(n)
        if choice==1:
            table=controller.getDataCCF()
            print(f'\n{tabulate(table, tablefmt="grid", maxcolwidths=[15, 30, 20, None, None, 10, None, 25, 30])}\n')
            print("Nhấn enter để tiếp tục: ", end =" ")
            temp=input()
            returned_value = os.system('cls')
        elif choice==2:
            table=controller.getDataLixAhead()
            print(f'\n{tabulate(table, tablefmt="grid", maxcolwidths=[None, 20, None, None, None, 50])}\n') 
            print("Nhấn enter để tiếp tục: ", end =" ")
            temp=input()
            returned_value = os.system('cls')
        elif choice==3:
            table=controller.getDataLixFuture()
            print(f'\n{tabulate(table, tablefmt="grid", maxcolwidths=[None, None, 15, 15, 30, 30, 30])}\n')
            print("Nhấn enter để tiếp tục: ", end =" ")
            temp=input()
            returned_value = os.system('cls')
        elif choice==4:
            table=controller.getDataLixPlanning()
            print(f'\n{tabulate(table, tablefmt="grid", maxcolwidths=[None, None, None, None, None, 30])}\n')
            print("Nhấn enter để tiếp tục: ", end =" ")
            temp=input()
            returned_value = os.system('cls')
        elif choice==5:
            table=controller.getDataLixRunning()
            print(f'\n{tabulate(table, tablefmt="grid")}\n')
            print("Nhấn enter để tiếp tục: ", end =" ")
            temp=input()
            returned_value = os.system('cls')
        elif choice==6:
            print("Nhập ID Conference: ", end =" ")
            conferenceID=input()

            table=controller.getFullname(conferenceID)
            print("\nTên đầy đủ hội nghị")
            print(f'{tabulate(table, tablefmt="grid")}\n') 

            print("Nhấn enter để tiếp tục: ", end =" ")
            temp=input()
            returned_value = os.system('cls')
        elif choice==7:
            print("Nhập từ khóa để tìm kiếm: ", end =" ")
            keyword=input()

            table=controller.searchCCFConference(keyword)
            print("\nThông tin hội nghị CCF")
            print(f'{tabulate(table, tablefmt="grid", maxcolwidths=[15, 30, 20, None, None, 10, None, 25, 30])}\n') 

            table=controller.searchHeadConference(keyword)
            print("\nThông tin hội nghị Lix Ahead")
            print(f'{tabulate(table, tablefmt="grid", maxcolwidths=[None, 20, None, None, None, 50])}\n') 

            table=controller.searchFutureConference(keyword)
            print("\nThông tin hội nghị Lix Future")
            print(f'{tabulate(table, tablefmt="grid", maxcolwidths=[None, None, 15, 15, 30, 30, 30])}\n') 

            table=controller.searchPlanningConference(keyword)
            print("\nThông tin hội nghị Lix Planning")
            print(f'{tabulate(table, tablefmt="grid", maxcolwidths=[None, None, None, None, None, 30])}\n') 

            table=controller.searchRunningConference(keyword)
            print("\nThông tin hội nghị Lix Running")
            print(f'{tabulate(table, tablefmt="grid")}\n') 

            print("Nhấn enter để tiếp tục: ", end =" ")
            temp=input()
            returned_value = os.system('cls')
        elif choice==8:
            result=controller.updateDataCCF()
            print(result)
            print("Nhấn enter để tiếp tục: ", end =" ")
            temp=input()
            returned_value = os.system('cls')
        elif choice==9:
            result=controller.updateDataLix()
            print(result)
            print("Nhấn enter để tiếp tục: ", end =" ")
            temp=input()
            returned_value = os.system('cls')
        elif choice==10:
            result=controller.exportDataCCF()
            print(result)
            print("Nhấn enter để tiếp tục: ", end =" ")
            temp=input()
            returned_value = os.system('cls')
        elif choice==11:
            result=controller.exportDataLixAhead()
            print(result)
            print("Nhấn enter để tiếp tục: ", end =" ")
            temp=input()
            returned_value = os.system('cls')
        elif choice==12:
            result=controller.exportDataLixFuture()
            print(result)
            print("Nhấn enter để tiếp tục: ", end =" ")
            temp=input()
            returned_value = os.system('cls')
        elif choice==13:
            result=controller.exportDataLixPlanning()
            print(result)
            print("Nhấn enter để tiếp tục: ", end =" ")
            temp=input()
            returned_value = os.system('cls')
        elif choice==14:
            result=controller.exportDataLixRunning()
            print(result)
            print("Nhấn enter để tiếp tục: ", end =" ")
            temp=input()
            returned_value = os.system('cls')
        elif choice==15:
            break
        else:
            print("Nhập sai lựa chọn! lựa chọn đúng từ 1 đến 15")
            print("Nhấn enter để tiếp tục: ", end =" ")
            temp=input()
            returned_value = os.system('cls')

# from tabulate import tabulate
# table = [['col 1', 'col 2', 'col 3', 'col 4'], [1, 2222, 30, 500], [4, 55, 6777, 1]]
# print(tabulate(table))