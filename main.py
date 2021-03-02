

# re = 6048 - 1934 + 3205.704 - 484 + 10313.46 - 1145
# wh = 2824.21 - 1065
# sz = 954.768 - 673
# dic = {'tc': {'t2': 9000.0, 't1': 9000.0, 'wl': 8579.0, 'total': 26579.0}}
# print(re)
# total_short_stock_by_truck = re - 1750 - 350
# print(total_short_stock_by_truck)
# total = 26579 - 1750 - 350 - 9100 - 2800 - 4200 - 3850 - 350 - 4900
# print(total)
# t1 = 9000 - 1750 - 350 - 6900
# print(t1)
# t2 = 9000 - 2200 - 2800 - 4000
# print(t2)
# wl = 8579 - 200 - 3850 - 350 - 4900
# print(wl)
# c = 4268 + 4822 - 712
# print(c)
#
# dic2 = {'tc': {'t2': 0.0, 't1': 0.0, 'wl': 2194.0, 'total': 2194.0},
#         'bj': {'t2': 0.0, 't1': 0.0, 'wl': 487.0, 'total': 487.0}}


plant_dict = {'CNCD': {'max_best_target': 0, 'boat_target': 0.0, 'train_target': 1261.916, 'truck_target': 413.1, 'plant_ttl': 552, '': '', 'planed': 0, 'detail': [], 'truck_lb_target': 351.9, 'lb_tc': 1.2, 'T1': 0, 'T2': 0, 'WL': 0, 'source': 'TC'},
              'CNGNORTH': {'max_best_target': 0, 'boat_target': 0.0, 'train_target': 0.0, 'truck_target': 399.828, 'plant_ttl': 1375, '': '', 'planed': 0, 'detail': [], 'truck_lb_target': 385.99199999999996, 'lb_tc': 1.2, 'T1': 0, 'T2': 0, 'WL': 0, 'source': 'BJ'},
              'CNGZ': {'max_best_target': 0, 'boat_target': 0.0, 'train_target': 0.0, 'truck_target': 1472.772, 'plant_ttl': 1081, '': '', 'planed': 0, 'detail': [], 'truck_lb_target': 1417.5479999999998, 'lb_tc': 1.2, 'T1': 0, 'T2': 0, 'WL': 0, 'source': 'TC'},
              'CNSZ': {'max_best_target': 0, 'boat_target': 0.0, 'train_target': 0.0, 'truck_target': 327.228, 'plant_ttl': 124, '': '', 'planed': 0, 'detail': [], 'truck_lb_target': 314.952, 'lb_tc': 1.2, 'T1': 0, 'T2': 0, 'WL': 0, 'source': 'TC'},
              'CNTC-GSH': {'max_best_target': 0, 'boat_target': 0.0, 'train_target': 0.0, 'truck_target': 1470.8400000000001, 'plant_ttl': 2211, '': '', 'planed': 0, 'detail': [], 'truck_lb_target': 1312.6799999999998, 'lb_tc': 1.2, 'T1': 0, 'T2': 0, 'WL': 0, 'source': 'TC'},
              'CNWH': {'max_best_target': 0, 'boat_target': 0.0, 'train_target': 2706.5999999999995, 'truck_target': 593.6160000000001, 'plant_ttl': 564, '': '', 'planed': 0, 'detail': [], 'truck_lb_target': 472.58399999999995, 'lb_tc': 1.2, 'T1': 0, 'T2': 0, 'WL': 0, 'source': 'BJ'}}


# total_short_stock_by_truck = sum([i['train_target'] - i['plant_ttl'] - i['planed'] for i in plant_dict.values() if i['train_target'] - i['plant_ttl'] - i['planed'] > 0])
# print(total_short_stock_by_truck)
#
# def get_total_short_stock_by_train(source):
#     total_short_stock_by_train = 0
#     for i in plant_dict.values():
#         if i["source"] == source:
#             if i['train_target'] - i['plant_ttl'] - i['planed'] > 0:
#                 total_short_stock_by_train += i['train_target'] - i['plant_ttl'] - i['planed']
#     return total_short_stock_by_train
#
#
# re = get_total_short_stock_by_train('BJ')
# print(re)



