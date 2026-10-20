"""Regenerate browser data, source coverage map, and teacher answer key."""
from pathlib import Path
import json
root=Path(__file__).resolve().parents[1]
d=json.loads((root/'data/course.json').read_text())
(root/'data/course.js').write_text('window.ASRIYAH_COURSE='+json.dumps(d,ensure_ascii=False,separators=(',',':'))+';')
coverage=['# Source and exercise coverage','',d['coverage']['statement'],'','PDF pages refer to the supplied files. Printed pages refer to the books. The source contents page has several inaccurate Part 2 page references; the map uses the actual lesson headers.','','| Part | Lesson | Title | PDF pages | Printed pages | Groups | Answer components | Status |','|---|---|---|---|---|---|---|---|']
key=['# الطريقة العصرية: تدریسی جواب نامہ','','Prepared by Dr. Imran Hayat — الحیات مرکز علوم اسلامیہ','','یہ تدریسی جواب نامہ فراہم کردہ دونوں حصوں کی اصل مشقوں کے ساتھ استعمال کریں۔ آزاد انشا، ذاتی تعارف اور ذاتی خط کے جواب قابل تبدیلی نمونے ہیں۔ اعراب یا معنی کی متعدد درست صورتیں ہو سکتی ہیں؛ سوال کا سیاق قائم رکھیں۔','']
for l in d['lessons']:
 count=sum(len(g['items']) for g in l['sourceSolutions'])
 coverage.append(f"| {l['part']} | {l['number']} | {l['titleUr']} | {l['pdfPages'][0]}–{l['pdfPages'][-1]} | {l['printedPages'][0]}–{l['printedPages'][-1]} | {len(l['sourceSolutions'])} | {count} | {l['sourceExerciseStatus']} |")
 key.extend([f"## حصہ {l['part']} — سبق {l['number']}: {l['titleUr']}",'',f"اصل PDF صفحات: {l['pdfPages'][0]}–{l['pdfPages'][-1]}؛ مطبوعہ صفحات: {l['printedPages'][0]}–{l['printedPages'][-1]}",''])
 for g in l['sourceSolutions']:
  key.extend([f"### {g['number']}. {g['title']}",'',f"PDF صفحہ {g['pdfPage']}؛ کتاب کا صفحہ {g['printedPage']}",'',g['explanation'],''])
  for i,item in enumerate(g['items'],1):key.extend([f"**{i}. سوال:** {item['prompt']}",'',f"**حل:** {item['answer']}",'',f"**وضاحت:** {item['explanation']}",''])
(root/'COVERAGE.md').write_text('\n'.join(coverage)+'\n');(root/'TEACHER_KEY.md').write_text('\n'.join(key)+'\n')
print(json.dumps(d['coverage'],ensure_ascii=False))
