# ADVANCED Project L1 

In file baraye in hast k yadavari shavad daghighan chikar krdim

# Overview
Yek app mikhaym besazim 
App -> GUI + Backend (infrustructure)
in app baraye **quiz management** tarahi shode. be goone ee k do ghesmat darim yek ghesmat soal ha va gozine ha tarahi mishe, yek file ham daneshjoo javab mide.


az topic haye zir estefade mishe
- **Python**
- **Function-based** 
- **ORM**
- **Database**
- **partial microservice**


# Sakhtare in app ch shekli mibasha
bebinid ma dar asl yek file README.md darim k hamin file hast ke tozihat neeveshte shdoe ast
yek file **database.py** darim k configuration database oonja hast va niazi b taghir nadare
yek ghesmat **models.py** darim k table ha va jadavel neveshte shdoe k niazi b taghirat nadare
file **crud.py** yekseri function dare k ejaze mide shoma rooye table haye database *write* va *read* anjam bedid.

```bsh
FANAVARI0226
|
|------README.md #tozihate app in to hast install, implement , run bshe
|----requirements.txt  #tamame dependency ketabkhone ,,....
|-----database.py #databasemon ro shoro mikonam (initialization)
|----models.py  #jadval hat (table) ha inja hastan
|----crud.py   #ejaze mide ma roye database ha amaliat anjam bdim tavabe amadan
|----seed.py  #question hainja matrah mishe va skahte msihe tooye db
|----main.py  #file i hast k (app) Run beshe soala porside o....

```

dar nahayat dota file bayad ejra beshe
- **seed.py**
in file dar asl shoma bazesh mikonid va soal matrah mikonid ba gozine ha
- **main.py** 
bad az tarahie soal ,inja mesle CLI hast ke daneshjoo javab mide be soalat


## Database
tooye python yek zarf 
```python
esm = 'ali'
```
RAM zakhrie mishe, agar kasi khamosh kone laptob, barname ro bebande
koelsh mire

opas ma mikhahim yeksri data koja zakhrie?--> Hard ->hamishe bashe
hamishe zakhrie bashe
Write, read konid



--> yek jaee hast k koli tabel tooshe , user pass dre, usere in db 
db --> jadval --> row , column (values)

mysql , sqlite , postgre ,.... 
zaban hesab 
tooye terminaleton --> codd zni d-->jadval ...

python vghty yek adado bekhayd zakhrie konid -> ketabkhone mysql-python sqlite-python 
va tavabe b goone ee enevshte shdoe --> 

```python
data = mysql.excute('select * from table')
```

#### **ORM anjam bdid**
databse ha begone e neevshgte msieh class ha --> k bejay einke inkaro koni

```python
USER
USER.add(data)
USER.show()
```


### requirements
ketabkhone hast --> ORM
```bsh
pip install SQLalchemy
```


## Database ro sakhtim
ma raftim yek fiel sakhtim be esme **database.py** toosh omadim
yek db sakhtim --> db khali 


## Jadval haro koja besazim?
yek file msiazim **models.py** va inja jadval haro takmilesh mikonim

ma yekseri jadval niaz darim
- **user**
- **questions**
- **choice**
- **answer**

```python
'''
Jadval --> Esme jadval User

--> id , name , answers 


----users------
id  | name | answers |
1   | ali  | 1,2,3   |
2   | reza | 2,1,4   |
3   | ahmad| 7,8,9   |


----questions----
id | text                | choices   |answer |
1  | manie fahmidan chis?| [1, 2, 3] |  3    |
2  | what is 2+2? | [4, 5, 6] | 6    |
3  | what is2*2? | [4, 5, 6] | 4    |
4  | what is2/2? | [1, 2, 3] | 1    |
5  | what is2**2? | [4, 5, 6] | 4   |
6  | what is2%2? | [0, 1, 2]  | 0   |
7  | what is2//2? | [0, 1, 2] | 0   |
8  | what is2**2? | [4, 5, 6] | 4   |
9  | what is2%2? | [0, 1, 2]  | 0 |
10  | what is2//2? | [0, 1, 2] | 0 |



-----choice----
id | text     | is_correct | question_id | question | 
1  | fahmidan | True      |  1        | manie fahmidan chis? |
2 | shenidan  | False     | 1         | manie fahmidan chis? |
3 |khordan    | False     | 1         | manie fahmidan chis? |
4 | 8         | True      | 2         | what is 2+2? |
5 | 7         | False     | 2         | what is 2+2? |
6 | 4         | True      | 2         | what is 2+2? |


-----Answers-----
id  |user_id | question_id | choice_id |
1  | ali     | 1         | 3         | 
2  | reza    | 2         | 6         | 
3  | ahmad   | 3         | 9         | 
4  | ali     | 4         | 8         | 
5  | reza    | 5         | 7         | 
6  | ahmad   | 6         | 4         | 
7  | ali     | 7         | 3         | 
8  | reza    | 8         | 2         | 
9  | ahmad   | 9         | 1         | 
10 | ali     | 10        | 0         | 

'''
```

sqlalchemy -->ketabkhone hast k ma install mikonim
jadval-->esm dare , soton dare (esm daran) ,type drn
sotonet adadi , str, float , ....



## **Crud.py**

in yek file hast koli tabe hats
in tavabe vase ine ke ma btonim adad varede database konim ya
azash kahrej konim
ki bokone ki nakone mohem nis

function ha in ejazaro bema mide



## seed.py

inja shoma question haro matrah mikoni
- question besazi 
- choice beszi

yek bar run mishe
- dataabse ro misaze, jadval haro miszr
** database.py -->tarif mikone engine
tooye seed.py --> misazish


## main.py 
ino daneshjoo, danesh amooz run mikone

- user miad
- mige soal haro neshonam bede
- done done javab mide






# Takalife shoma

- estefade
- seed.py --> 4 ta soal ezafe konid
- main.py --> run konid javab bdid


- 3 ta function crud.py




#----- Tarigheye kar
```bsh
FANAVARI0226
|
|------README.md #tozihate app in to hast install, implement , run bshe
|----requirements.txt  #tamame dependency ketabkhone ,,....
|-----database.py #databasemon ro shoro mikonam (initialization)
|----models.py  #jadval hat (table) ha inja hastan
|----crud.py   #ejaze mide ma roye database ha amaliat anjam bdim tavabe amadan
|----seed.py  #question hainja matrah mishe va skahte msihe tooye db
|----main.py  #file i hast k (app) Run beshe soala porside o....

```

baraye inke shoro konid 
#### 1- Install
```bsh
pip install SQLalchemy
```

```bsh
python seed.py
```


#### 2-Run app
```bsh
python main.py
```
yekbar 4 ta soal ezafe konid b seed.py
main.py -->yekbar shode run koni

3 ta function dar crud.py besazid

DOHAFTE zaman hast


# Koja bargozari konim?
dakhele Github bayad bargozari konid
ke dakheel file [github_tutorial](github_tutorial.md) tozih dade shode



