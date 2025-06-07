def dem_so_lan_xuat_hien(lst):
    count_dict = {}
    for num in lst:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    return count_dict

input_list = input("Nhập danh sách số nguyên cách nhau bởi dấu cách: ")
numbers = list(map(int, input_list.split()))
so_lan_xuat_hien = dem_so_lan_xuat_hien(numbers)
print("Số lần xuất hiện của các phần tử trong danh sách:", so_lan_xuat_hien)