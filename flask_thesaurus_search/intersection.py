from .crawl_data_onelook_official import *
from .crawl_data_thesaurus_official import *
from .crawl_data_glosbe_official import *


def common_member(a, b, c): 
      
    a_set = set(a) 
    b_set = list(b) + list(c)
      

    if len(a_set.intersection(b_set)) > 0: 
        return(a_set.intersection(b_set))   
    else: 
        return("no common elements") 
tu_tuong_dong    = list(common_member(tu_dong_nghia, symnonym_list, symnonym_list_glosbe))
merge_list       = tu_dong_nghia + symnonym_list_glosbe + symnonym_list 
set_tu_lap_lai   = set([item for item in merge_list if merge_list.count(item) > 1])
tu_lap_lai       = list(set_tu_lap_lai)

final_list = []
for _1 in tu_tuong_dong:
    final_list.append(_1)
for _2 in tu_lap_lai:
    if _2 not in tu_tuong_dong:
        final_list.append(_2)
for _3 in merge_list:
    if _3 not in tu_tuong_dong and _3 not in tu_lap_lai:
        final_list.append(_3)

print(final_list)