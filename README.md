## Keyboard Typing User Recognition
#### Short description

This project aims for user recognition based on keyboard typing patterns using machine learning [kNN](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm) algorithm,  data based on flight and dwell time for keystrokes. 

In future there could be more algorithms implemented just for fun with some clarification in docs.

#### Requirements

* Linux/Mac/Windows
* Python3.5
* pip3

#### Usage
```sh
python3 app.py
```
 
 
 
## Description
### Data structure

Data was gathered via web page. Every analyzed record in database has that scheme:
```sql
INSERT INTO `user_typing_data` (`time`, `user_id`, `input0`, `IP`, `browser`) 
VALUES
('2013-11-20 07:25:12', 7, 'd_190_0_0 u_190_64 d_84_1008_1 u_84_1063
d_73_1776_2 u_73_1832 d_69_1872_3 u_69_1952 d_53_3128_4 u_53_3176
d_16_5256_5 d_82_5424_5 u_82_5464 u_16_5672 d_79_7303_6 u_79_7359
d_65_10167_7 u_65_10223 d_78_11420_8 u_78_11439 d_76_11679_9
u_76_11719 d_13_12156_10 u_13_12183 ', '81.219.51.76', 'Mozilla/5.0 (Windows
NT 5.1; rv:24.0) Gecko/20100101 Firefox/24.0'),
```
#
***input0*** field is list of items like that one: 
 
```
(d/u)_keycode_time[_caret]
```
 
**d/u** - *pressed/released action* 
 
**keycode** - *js keycode* 
 
**time** - *time elapsed from first pressed button (in ms)* 
 
**caret** - *caret position* 
 
 
### Data preprocessing

To extract only valuable numeric info about keyboard typing pattern, we process data to be list of items ***flight time*** (time button being pressed) and ***dwell time*** (time between pressing button) like this:
```
[60, 135, 60, 70, 39, 46, 79, 274, 80, 235, 59, 44, 81]
```

This trick makes two lists easy to compare using some metric for example ***Manhattan*** one.
After that we can just use kNN algorithm which is widely described.

### Results
Using kNN algorithm with ***k=5***, effects below:

Test nr     | Accuracy
------------- | ------------
1 | 0.867950
2 | 0.872765
3 | 0.842503
4 | 0.864512
5 | 0.861761
6 | 0.871389
7 | 0.867950
8 | 0.863824

For further extending algorithms there is multiple things which can be done to gain more accuracy, for example using ***IP address***, ***user-agent*** or ***time*** when website was visited.


### Results #2
Exteding distance using above parameters with some wages give quite nice accuracy improvement:

Test nr     | Accuracy
------------- | ------------
1 | 0.936726
2 | 0.928473
3 | 0.940853
4 | 0.936726
5 | 0.927098
6 | 0.933975
7 | 0.931912
8 | 0.936039

It is possible to better adjust wages for parameters and gain more accuracy
