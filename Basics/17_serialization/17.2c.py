# -*- coding: utf-8 -*-
import glob,pprint
from draw_network_graph import draw_topology
from task17_2b import generate_topology_from_cdp

sh_cdp_n_files = glob.glob('sh_cdp_n*')
topology_fin = generate_topology_from_cdp(sh_cdp_n_files)

def topology_translate(topology_in):
    global topology_fin
    new_dict = {}
    for key in topology_fin.keys():
        print(key)
        #print(topology_fin[key])
        for key2 in topology_fin[key]:
            #print(key2)
            #print(topology_fin[key][key2])
            #print(tuple(topology_fin[key][key2].items()))
            for item in topology_fin[key][key2].items():
                new_dict_string = {(key, key2): item}
                new_dict.update(new_dict_string)
                new_dict_string = {}

        for key in new_dict.copy().keys():
            for value in new_dict.copy().values():
                if key == value:
                    print(key, value)
                    del (new_dict[key])

        topology_out = new_dict
    #print(new_dict)
    return topology_out

topology_dict = topology_translate(sh_cdp_n_files)

print(topology_dict)

draw_topology(topology_dict)

'''
Задание 17.2c

С помощью функции draw_topology из файла draw_network_graph.py
сгенерировать топологию, которая соответствует описанию в файле topology.yaml

Обратите внимание на то, какой формат данных ожидает функция draw_topology.
Описание топологии из файла topology.yaml нужно преобразовать соответствующим образом,
чтобы использовать функцию draw_topology.

Для решения задания можно создать любые вспомогательные функции.

Не копировать код функции draw_topology.

В итоге, должно быть сгенерировано изображение топологии.
Результат должен выглядеть так же, как схема в файле task_10_2c_topology.svg

При этом:
* Интерфейсы могут быть записаны с пробелом Fa 0/0 или без Fa0/0.
* Расположение устройств на схеме может быть другим
* Соединения должны соответствовать схеме


> Для выполнения этого задания, должен быть установлен graphviz:
> apt-get install graphviz

> И модуль python для работы с graphviz:
> pip install graphviz

'''
