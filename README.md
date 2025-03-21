# README: PM 2.5 Forecasting Model

## Model Saving
- บันทึกโมเดลเป็นไฟล์ `Model.pkl`
- บันทึกข้อมูลตัวแปรภายนอก (`X_forecast`) เป็นไฟล์ `model.csv`

## DashBord
- นำไฟล์ที่บันทึกมาพยากรณ์และแสดงผลบนหน้า Dash

## Install Dependencies
- ก่อนใช้งาน ให้ติดตั้งไลบรารีที่จำเป็นโดยใช้คำสั่งต่อไปนี้:

```bash
pip install -r requirements.txt
```

## Run Programe
- หลังจากติดตั้งเสร็จแล้ว สามารถรันเซิร์ฟเวอร์ Dash ได้โดยใช้คำสั่ง:

```bash
python app.py
```

## Activate the system
- เมื่อรันสำเร็จ ระบบจะแสดงผลที่ **http://127.0.0.1:8050/** หรือพอร์ตที่กำหนดไว้

## More
- ใช้โมเดล **Auto ARIMA** จาก **PyCaret** สำหรับพยากรณ์ค่า PM2.5
- ไฟล์ **Model.pkl** จะใช้เก็บโมเดลที่ผ่านการเทรน (โค้ดส่วนนี้ถูกคอมเมนต์ไว้ก่อน)
- การแสดงผลข้อมูลใช้ **Plotly** และ **Dash Leaflet** หรือ **Mapbox** สำหรับแผนที่

---
**ผู้พัฒนา:** *[PATTARAPONG]* AND  *[PEERANAT]*


