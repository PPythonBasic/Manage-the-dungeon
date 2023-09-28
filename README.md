# โปรแกรมจัดการดันเจียน
</div>

### การทำงานของโปรแกรมนี้
- ให้ทำการวนซ้ำสามารถเลือกได้เรื่อยๆจนกว่าจะพิมพ์ 0
```
         <|Manage The Dungeon|>         
[1] Add items to the dungeon
[2] View items in the dungeon
[3] Let the hero enter the dungeon
[0] Close the dungeon
Choice : 0
```
### อธิบาย
รูปแบบตัวอย่างข้อมูลที่จะถูกเก็บ
```
{'Item_name': '','Price':0,'Amount': 0}
```
- สร้างข้อมูลเก็บไว้เป็น list แบบ global หนึ่งตัว
- Add items to the dungeon คือการเพิ่มข้อมูลเข้าไปในดันเจี้ยน การแสดงผลก็จะเป็นเป็นดังนี้
```
Enter Item name : Sword
Enter Price : 200
Enter Amount : 1
-------
Sword 200G 1x
```
```
{'Item_name': 'Sword','Price':200,'Amount': 1}
```
หรือ
```
Enter Item name : HP
Enter Price : 50
Enter Amount : 1
-------
HP 50G 1x
```
```
{'Item_name': 'HP','Price':50,'Amount': 1}
```
```
Enter Item name : HP
Enter Price : 50
Enter Amount : 1
-------
HP 50G 1x
```
```
{'Item_name': 'HP','Price':50,'Amount': 1}
```
```
Enter Item name : HP
Enter Price : 50G
Enter Amount : 1
-------
HP 50G 1x
```
```
{'Item_name': 'HP','Price':50,'Amount': 1}
```

- View items in the dungeon คือการแสดงไอเทมทั้งหมดในดันเจี้ยนแสดงให้รูปแบบดังนี้
```
---- Show All Items in the Dungeon -----
- Sword 200G 1x
- HP 50G 1x
- HP 50G 1x
- HP 50G 1x
```
- Let the hero enter the dungeon คือการให้ผู้เล่นเข้ามาดันเจี้ยนโดยให้มีลักษณะการทำงานดังนี้
     * ผู้เล่นจะได้รับไอเทมจะได้มาจากการสุ่มไอเทม
     * เมื่อผู้เล่นได้รับไอเทมไปแล้วไอเทมที่อยู่ในคลังของดันเจี้ยนชิ้นนั้นก็จะถูกลดลงไปตามจำนวนที่ผู้เล่นได้ไป
     * จากนั้นแสดงผลดังนี้
```
Hero receives 1x Sword item.
```
หรือ
```
Hero receives 1x HP item.
```

### ฟังก์ชั่น
- จะมีฟังก์ชันที่มีมาให้ที่ไฟล์ manage_the_dungeon.py
```python
    def match_funct(choice:int):
        match choice:
            case 1:
                pass

    def run_dungeon():
        while True:
            print('<|Manage The Dungeon|>'.center(40," "))
            print('[1] Add items to the dungeon')
            print('[2] View items in the dungeon')
            print('[3] Let the hero enter the dungeon.')
            print('[0] Close the dungeon.')
            choice = input('Choice : ')
            match_funct(choice)
```
- ในไฟล์ main.py ไม่ต้องแก้ไขอะไรใช้ในการรันโปรแกรมอย่างเดียว
- 
### รันโปรแกรม
```
python3 main.py
```
หรือ
```
python main.py
```

# Implementation
- ทำการ `Fork` ให้เรียบร้อยปุ่มตามภาพด้านล่าง

<img src="https://cdn.discordapp.com/attachments/372372440334073859/1156568624388116654/image.png?ex=651571f8&is=65142078&hm=6955890a844d52e0d3b7527d9073f0811c6bc1d5231f4120809516d7f2b2436f&">

- ตั้งชื่อ repo ใหม่ (ไม่จำเป็น) จากนั้นกดปุ่ม `Create Fork`

<img align="center" src="https://cdn.discordapp.com/attachments/372372440334073859/1156569568760823858/image.png?ex=651572d9&is=65142159&hm=33d89652d11f893a1a48743efa9ac68a0a4f5330bb9c3f01a9d2e4245b3c4139&">

- ไปที่ปุ่ม `Code` คัดลอกลิงก์ดังรูป

<img align="center" src="https://cdn.discordapp.com/attachments/372372440334073859/1156570821775601796/305y5IV.png?ex=65157403&is=65142283&hm=3bb6a5c0537813df810ce84d3a25616e964d3e0d7581b5cc4bbaf4fe6f8aa2f1&">

- จากนั้นไปที่ Terminal หรือ cmd และทำการ cd ไปยัง drive ที่จะเก็บงาน
- ใช้คำสั่งดังนี้
```
git clone <url ที่คัดลอกมา>
```
```
cd Manage-the-dungeon
```
```
code .
```
- เริ่มเขียนโค้ดได้เลย
  
* `code .` คือกรณีใช้ vscode ใช้ VSCode

# Participation
- ทุกครั้งที่เขียนแต่ละฟังก์ชั่นเสร็จให้ทำการ `commit` ทุกครั้ง
- จากนั้นก็ทำการ `Pull Request` โดยไปที่หน้า repo ของคุณที่พึ่ง `Fork` ไปจากนั้นทำตามภาพ
![](https://cdn.discordapp.com/attachments/372372440334073859/1156573259232448552/6f14jIy.png?ex=65157649&is=651424c9&hm=974ba577b6848d81f98f1d051617f7a071dd6a6596cf2709a56894602ea88db2&)
- เลือก `New pull request`
![](https://cdn.discordapp.com/attachments/372372440334073859/1156573519803596910/image.png?ex=65157687&is=65142507&hm=a650722f6188d36455095de634f2d1decc76d7263d4615b4f2d55b45fb132398&)
- เลือก `Create pull request`
![](https://cdn.discordapp.com/attachments/372372440334073859/1156573856362922076/image.png?ex=651576d7&is=65142557&hm=4e539be01ec4ef80856b0865ab87ab4373da105c7197ed844c513657d7752b47&)
- ตั้งชื่อสิ่งที่เพิ่มเข้ามา จากนั้นเลือก `Create pull request` อีกครั้ง
![](https://cdn.discordapp.com/attachments/372372440334073859/1156574064001953802/image.png?ex=65157708&is=65142588&hm=3c2346880545bebaef1dd50412c9efbb2c098df7ac3b39f8e41a93e617a081e4&)
- เสร็จจากนั้นรอเจ้าของโครงการ commit

# การทดสอบ
- ติดตั้ง pytest โดยใช้คำสั่ง
```
pip install -r requirements.txt
```
- จากนั้นใช้คำสั่ง
```
pytest test.py --no-header --no-summary -v -s
```
- ถ้าผลรันผ่านแสดงว่าฟังก์ชันนั้นทำงานได้ดีถ้าไม่ผ่านก็ไปแก้โค้ด
