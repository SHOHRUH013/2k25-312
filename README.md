# Smart City — Loyihasi

Bu loyiha "Smart_City" papkasida joylashgan Python asosidagi modul va core komponentlardan iborat. Loyihaning maqsadi turli shahar tizimlarini (energiya, yoritish, xavfsizlik, transport) modul tarzida tashkil qilish va ularni boshqarish uchun arxitektura (builders, composite, controller, proxy, subsystem_factory) taqdim etishdir.

Tez boshlash
1. Virtual muhit yarating va aktivlashtiring:
   - python -m venv .venv
   - source .venv/bin/activate (Linux/macOS) yoki .venv\Scripts\activate (Windows)
2. Kutubxonalarni o'rnating (agar kerak bo'lsa):
   - pip install -r requirements.txt
3. Dasturiy nuqtai:
   - Loyihani ishga tushurish: `python Smart_City/main.py`
   - Savol-javob/review: `python Smart_City/qa.py`

Loyiha tuzilishi
- Smart_City/main.py — ilova boshlang'ich nuqtasi.
- Smart_City/qa.py — tezkor test yoki savol-javob skripti.
- Smart_City/core/ — arxitektura va dizayn pattern'lari:
  - builders.py
  - composite.py
  - controller.py
  - proxy.py
  - subsystem_factory.py
- Smart_City/modules/ — tizim modullari:
  - energy.py
  - lighting.py
  - security.py
  - transport.py

Qanday ishlaydi
- Har bir modul (modules/*.py) o'z subsystemini ifodalaydi.
- core ichidagi fayllar subsystemlarni qurish, birlashtirish va boshqarish uchun pattern'larni ta'minlaydi.
- main.py butun tizimni sozlab ishga tushiradi.
