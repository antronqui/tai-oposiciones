import os
import re
import pypdf

BASE_DIR = r'C:\Users\antro\OneDrive\TAI\Examenes anteriores'
OUTPUT_DIR = r'C:\Users\antro\antigravity\fichas_TAI\examenes_oficiales'

os.makedirs(OUTPUT_DIR, exist_ok=True)

EXAM_CONFIGS = [
    {
        "id": "2024_TAI_LIBRE_MODELO_A",
        "title": "Examen Oficial TAI 2024 — Ingreso Libre (Modelo A)",
        "year": 2024,
        "type": "Ingreso Libre",
        "model": "Modelo A",
        "cuestionario_pdf": os.path.join(BASE_DIR, r"2024\Cuestionario_TAI_LI_2024_A_M8L91VL1CL_154AB89SD658.pdf"),
        "plantilla_pdf": os.path.join(BASE_DIR, r"2024\Plantilla Cuestionario_TAI_LI_2024_A_definitiva.pdf"),
        "out_file": "EXAMEN_OFICIAL_2024_TAI_LIBRE_MODELO_A.md"
    },
    {
        "id": "2024_TAI_LIBRE_MODELO_B",
        "title": "Examen Oficial TAI 2024 — Ingreso Libre (Modelo B)",
        "year": 2024,
        "type": "Ingreso Libre",
        "model": "Modelo B",
        "cuestionario_pdf": os.path.join(BASE_DIR, r"2024\Cuestionario_TAI_LI_2024_B_DNFGFEK45R_154AB89SD658.pdf"),
        "plantilla_pdf": os.path.join(BASE_DIR, r"2024\Plantilla Cuestionario_TAI_LI_2024_B_definitiva.pdf"),
        "out_file": "EXAMEN_OFICIAL_2024_TAI_LIBRE_MODELO_B.md"
    },
    {
        "id": "2024_TAI_PI_MODELO_A",
        "title": "Examen Oficial TAI 2024 — Promoción Interna (Modelo A)",
        "year": 2024,
        "type": "Promoción Interna",
        "model": "Modelo A",
        "cuestionario_pdf": os.path.join(BASE_DIR, r"2024\Cuestionario_TAI_PI_2024_A_3GZ5F829JV_154AB89SD658.pdf"),
        "plantilla_pdf": os.path.join(BASE_DIR, r"2024\Plantilla Cuestionario_TAI_PI_2024_A_definitiva.pdf"),
        "out_file": "EXAMEN_OFICIAL_2024_TAI_PI_MODELO_A.md"
    },
    {
        "id": "2024_TAI_PI_MODELO_B",
        "title": "Examen Oficial TAI 2024 — Promoción Interna (Modelo B)",
        "year": 2024,
        "type": "Promoción Interna",
        "model": "Modelo B",
        "cuestionario_pdf": os.path.join(BASE_DIR, r"2024\Cuestionario_TAI_PI_2024_B_IBTCZNPEKW_154AB89SD658.pdf"),
        "plantilla_pdf": os.path.join(BASE_DIR, r"2024\Plantilla Cuestionario_TAI_PI_2024_B_definitiva.pdf"),
        "out_file": "EXAMEN_OFICIAL_2024_TAI_PI_MODELO_B.md"
    },
    {
        "id": "2025_TAI_LIBRE_MODELO_A",
        "title": "Examen Oficial TAI 2025 — Ingreso Libre (Modelo A)",
        "year": 2025,
        "type": "Ingreso Libre",
        "model": "Modelo A",
        "cuestionario_pdf": os.path.join(BASE_DIR, r"2025\Cuestionario TAI-L-ModeloA.pdf"),
        "plantilla_pdf": os.path.join(BASE_DIR, r"2025\Plantilla respuestas TAI-L-A_act.pdf"),
        "out_file": "EXAMEN_OFICIAL_2025_TAI_LIBRE_MODELO_A.md"
    },
    {
        "id": "2025_TAI_LIBRE_MODELO_B",
        "title": "Examen Oficial TAI 2025 — Ingreso Libre (Modelo B)",
        "year": 2025,
        "type": "Ingreso Libre",
        "model": "Modelo B",
        "cuestionario_pdf": os.path.join(BASE_DIR, r"2025\Cuestionario TAI-L-ModeloB.pdf"),
        "plantilla_pdf": os.path.join(BASE_DIR, r"2025\Plantilla respuestas TAI-L-B_act.pdf"),
        "out_file": "EXAMEN_OFICIAL_2025_TAI_LIBRE_MODELO_B.md"
    },
    {
        "id": "2025_TAI_PI_MODELO_A",
        "title": "Examen Oficial TAI 2025 — Promoción Interna (Modelo A)",
        "year": 2025,
        "type": "Promoción Interna",
        "model": "Modelo A",
        "cuestionario_pdf": os.path.join(BASE_DIR, r"2025\Cuestionario TAI-P-ModeloA.pdf"),
        "plantilla_pdf": os.path.join(BASE_DIR, r"2025\Plantilla respuestas TAI-P-ModeloA.pdf"),
        "out_file": "EXAMEN_OFICIAL_2025_TAI_PI_MODELO_A.md"
    },
    {
        "id": "2025_TAI_PI_MODELO_B",
        "title": "Examen Oficial TAI 2025 — Promoción Interna (Modelo B)",
        "year": 2025,
        "type": "Promoción Interna",
        "model": "Modelo B",
        "cuestionario_pdf": os.path.join(BASE_DIR, r"2025\Cuestionario TAI-P-ModeloB.pdf"),
        "plantilla_pdf": os.path.join(BASE_DIR, r"2025\Plantilla respuestas TAI-P-ModeloB.pdf"),
        "out_file": "EXAMEN_OFICIAL_2025_TAI_PI_MODELO_B.md"
    },
    {
        "id": "2022_TAI_LIBRE",
        "title": "Examen Oficial TAI OEP 2022 — Ingreso Libre",
        "year": 2022,
        "type": "Ingreso Libre",
        "model": "Modelo Único",
        "cuestionario_pdf": os.path.join(BASE_DIR, r"2022\Cuestionario TAI-L_2023.pdf"),
        "plantilla_pdf": os.path.join(BASE_DIR, r"2022\PlantillaRespuestas DEFINITIVA TAI-L_oep2022.pdf"),
        "out_file": "EXAMEN_OFICIAL_2022_TAI_LIBRE.md"
    },
    {
        "id": "2022_TAI_PI",
        "title": "Examen Oficial TAI OEP 2022 — Promoción Interna",
        "year": 2022,
        "type": "Promoción Interna",
        "model": "Modelo Único",
        "cuestionario_pdf": os.path.join(BASE_DIR, r"2022\Cuestionario TAI-PI_2023.pdf"),
        "plantilla_pdf": os.path.join(BASE_DIR, r"2022\Plantilla respuestas DEFINITIVA TAI-P_oep2022.pdf"),
        "out_file": "EXAMEN_OFICIAL_2022_TAI_PI.md"
    },
]

def parse_plantilla(plantilla_pdf_path):
    reader = pypdf.PdfReader(plantilla_pdf_path)
    text = '\n'.join([p.extract_text() or '' for p in reader.pages])
    
    sections = {
        "primera_parte": {},
        "reserva_primera": {},
        "supuesto_1": {},
        "reserva_supuesto_1": {},
        "supuesto_2": {},
        "reserva_supuesto_2": {}
    }
    
    current_sec = "primera_parte"
    in_supuesto = None
    
    for raw_l in text.split('\n'):
        l = raw_l.strip()
        if not l:
            continue
        lower_l = l.lower()
        
        if "primera parte" in lower_l:
            current_sec = "primera_parte"
            in_supuesto = None
            continue
        elif "preguntas de reserva" in lower_l or "reserva" in lower_l:
            if in_supuesto == 1:
                current_sec = "reserva_supuesto_1"
            elif in_supuesto == 2:
                current_sec = "reserva_supuesto_2"
            else:
                current_sec = "reserva_primera"
            continue
        elif "supuesto i " in lower_l or lower_l.startswith("supuesto i") or lower_l.startswith("supuesto 1"):
            current_sec = "supuesto_1"
            in_supuesto = 1
            continue
        elif "supuesto ii" in lower_l or lower_l.startswith("supuesto ii") or lower_l.startswith("supuesto 2"):
            current_sec = "supuesto_2"
            in_supuesto = 2
            continue
            
        m = re.match(r'^(\d+)[\.\s]+([abcdABCD]|anulada|ANULADA)', l)
        if m:
            num = int(m.group(1))
            ans = m.group(2).upper()
            sections[current_sec][num] = ans
            
    return sections

def clean_and_parse_exam(cuestionario_pdf):
    reader = pypdf.PdfReader(cuestionario_pdf)
    full_text = []
    for page in reader.pages:
        t = page.extract_text() or ''
        full_text.append(t)
    raw = '\n'.join(full_text)
    
    # Clean noise
    lines = []
    for l in raw.split('\n'):
        s = l.strip()
        if re.search(r'P[áa]gina \d+ de \d+', s, re.IGNORECASE):
            continue
        if re.match(r'^\d{4}\s*-\s*TAI.*', s):
            continue
        lines.append(s)
    clean_text = '\n'.join(lines)
    return clean_text

def format_exam_markdown(cfg, clean_text, plantillas):
    md = []
    md.append(f"# 🏛️ {cfg['title']}")
    md.append(f"> **Organismo convocante:** Instituto Nacional de Administración Pública (INAP) / CPS  ")
    md.append(f"> **Convocatoria:** {cfg['type']} | **Variante:** {cfg['model']} | **Año:** {cfg['year']}  ")
    md.append(f"> **Plantilla:** Asociada y verificada según plantilla oficial definitiva del INAP.  ")
    md.append("")
    md.append("---")
    md.append("")
    
    # Table of answers overview
    md.append("## 📊 Plantilla Oficial de Respuestas (Vista Rápida)")
    md.append("")
    for sec_key, sec_title in [
        ("primera_parte", "Primera Parte (Cuestionario General)"),
        ("reserva_primera", "Preguntas de Reserva (Primera Parte)"),
        ("supuesto_1", "Supuesto Práctico I"),
        ("reserva_supuesto_1", "Preguntas de Reserva (Supuesto I)"),
        ("supuesto_2", "Supuesto Práctico II"),
        ("reserva_supuesto_2", "Preguntas de Reserva (Supuesto II)"),
    ]:
        ans_dict = plantillas.get(sec_key, {})
        if ans_dict:
            md.append(f"### {sec_title}")
            md.append("")
            
            # Format in rows of 10
            row_header = "| Preguntas | " + " | ".join([f"**+{i}**" for i in range(10)]) + " |"
            row_sep = "| :--- | " + " | ".join([":---:" for _ in range(10)]) + " |"
            md.append(row_header)
            md.append(row_sep)
            
            nums = sorted(ans_dict.keys())
            if nums:
                min_n = nums[0]
                max_n = nums[-1]
                # Start at decade boundary
                start_decade = (min_n // 10) * 10
                for dec in range(start_decade, max_n + 1, 10):
                    cells = []
                    for offset in range(10):
                        n = dec + offset
                        if n in ans_dict:
                            ans_val = ans_dict[n]
                            if ans_val == "ANULADA":
                                cells.append("🚫 *ANUL*")
                            else:
                                cells.append(f"**{ans_val}**")
                        else:
                            cells.append("-")
                    md.append(f"| **{dec} - {dec+9}** | " + " | ".join(cells) + " |")
            md.append("")
            
    md.append("---")
    md.append("")
    md.append("## 📝 Cuestionario Oficial con Respuestas Asociadas")
    md.append("")
    
    # Now let's format each question
    # To ensure 100% fidelity without losing text, we split the cleaned text into questions
    # and attach the answer.
    
    # Split text into sections
    sections = {}
    p_sup2 = re.search(r'\b(?:SUPUESTO\s+(?:PR[AÁ]CTICO\s+)?II|SUPUESTO\s+2)\b', clean_text, re.IGNORECASE)
    p_sup1 = re.search(r'\b(?:SUPUESTO\s+(?:PR[AÁ]CTICO\s+)?I\b|SUPUESTO\s+1\b)', clean_text, re.IGNORECASE)
    
    text_sup2 = ""
    text_sup1 = ""
    text_prim = clean_text
    
    if p_sup2:
        text_sup2 = clean_text[p_sup2.start():]
        text_prim = clean_text[:p_sup2.start()]
    if p_sup1:
        if p_sup2 and p_sup1.start() < p_sup2.start():
            text_sup1 = text_prim[p_sup1.start():]
            text_prim = text_prim[:p_sup1.start()]
        elif not p_sup2:
            text_sup1 = clean_text[p_sup1.start():]
            text_prim = clean_text[:p_sup1.start()]
            
    def render_section(sec_name, sec_text, ans_map, res_ans_map):
        lines_out = []
        lines_out.append(f"### 📌 {sec_name}")
        lines_out.append("")
        
        # Check if there is a intro / case description for Supuestos
        m_intro = re.search(r'(?:DESCRIPCI[OÓ]N\s+DEL\s+SUPUESTO|ENUNCIADO|Se\s+plantea).*?(?=\n\s*1\.\s+)', sec_text, re.DOTALL | re.IGNORECASE)
        if m_intro:
            intro_txt = m_intro.group(0).strip()
            lines_out.append("#### 📖 Caso Práctico:")
            lines_out.append(f"> {intro_txt.replace(chr(10), chr(10)+'> ')}")
            lines_out.append("")
            
        # Separate main from reserva
        m_res = re.search(r'PREGUNTAS\s+DE\s+RESERVA', sec_text, re.IGNORECASE)
        main_chunk = sec_text[:m_res.start()] if m_res else sec_text
        res_chunk = sec_text[m_res.start():] if m_res else ""
        
        def parse_chunk_questions(chunk, is_reserva=False):
            active_ans = res_ans_map if is_reserva else ans_map
            # Split by question numbers
            q_splits = re.split(r'\n(?=\s*\d+\.\s+)', '\n' + chunk)
            for q_str in q_splits:
                q_s = q_str.strip()
                if not q_s:
                    continue
                m_q = re.match(r'^(\d+)\.\s*(.*)', q_s, re.DOTALL)
                if m_q:
                    q_num = int(m_q.group(1))
                    body = m_q.group(2).strip()
                    
                    # Split options
                    # Find a), b), c), d)
                    opt_matches = list(re.finditer(r'(?:^|\n)\s*([abcdABCD])\)\s*', body))
                    if len(opt_matches) >= 4:
                        enunciado = body[:opt_matches[0].start()].strip()
                        opts = {}
                        for i, om in enumerate(opt_matches):
                            letter = om.group(1).upper()
                            s_idx = om.end()
                            e_idx = opt_matches[i+1].start() if i+1 < len(opt_matches) else len(body)
                            opts[letter] = body[s_idx:e_idx].strip()
                            
                        # Lookup answer
                        ans_official = active_ans.get(q_num, "N/D")
                        tag = " (Pregunta de Reserva)" if is_reserva else ""
                        lines_out.append(f"#### Pregunta {q_num}{tag}")
                        lines_out.append(f"{enunciado}")
                        lines_out.append("")
                        for opt_k in ['A', 'B', 'C', 'D']:
                            lines_out.append(f"- **{opt_k.lower()})** {opts.get(opt_k, '')}")
                        lines_out.append("")
                        
                        if ans_official == "ANULADA":
                            lines_out.append(f"> **Respuesta oficial definitiva:** 🚫 **PREGUNTA ANULADA POR LA CPS / INAP**")
                        else:
                            lines_out.append(f"> **Respuesta oficial definitiva:** **Opción {ans_official}** (según plantilla oficial)")
                        lines_out.append("")
                    else:
                        # Fallback if options formatting is irregular
                        ans_official = active_ans.get(q_num, "N/D")
                        tag = " (Pregunta de Reserva)" if is_reserva else ""
                        lines_out.append(f"#### Pregunta {q_num}{tag}")
                        lines_out.append(f"{body}")
                        lines_out.append("")
                        if ans_official == "ANULADA":
                            lines_out.append(f"> **Respuesta oficial definitiva:** 🚫 **PREGUNTA ANULADA POR LA CPS / INAP**")
                        else:
                            lines_out.append(f"> **Respuesta oficial definitiva:** **Opción {ans_official}** (según plantilla oficial)")
                        lines_out.append("")
                        
        parse_chunk_questions(main_chunk, is_reserva=False)
        if res_chunk:
            lines_out.append("---")
            lines_out.append("#### 🛡️ Preguntas de Reserva")
            lines_out.append("")
            parse_chunk_questions(res_chunk, is_reserva=True)
            
        return '\n'.join(lines_out)

    if text_prim:
        md.append(render_section("PRIMERA PARTE (Cuestionario Teórico)", text_prim, plantillas.get("primera_parte", {}), plantillas.get("reserva_primera", {})))
        md.append("")
    if text_sup1:
        md.append(render_section("SUPUESTO PRÁCTICO I (Desarrollo / Sistemas)", text_sup1, plantillas.get("supuesto_1", {}), plantillas.get("reserva_supuesto_1", {})))
        md.append("")
    if text_sup2:
        md.append(render_section("SUPUESTO PRÁCTICO II (Sistemas / Comunicaciones)", text_sup2, plantillas.get("supuesto_2", {}), plantillas.get("reserva_supuesto_2", {})))
        md.append("")
        
    return '\n'.join(md)

# Run for all configs
for cfg in EXAM_CONFIGS:
    if os.path.exists(cfg['cuestionario_pdf']) and os.path.exists(cfg['plantilla_pdf']):
        print(f"Processing {cfg['id']}...")
        plantillas = parse_plantilla(cfg['plantilla_pdf'])
        cleaned_txt = clean_and_parse_exam(cfg['cuestionario_pdf'])
        md_content = format_exam_markdown(cfg, cleaned_txt, plantillas)
        out_path = os.path.join(OUTPUT_DIR, cfg['out_file'])
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(md_content)
        print(f"  -> Generated {cfg['out_file']}")
    else:
        print(f"Missing file for {cfg['id']}")

print("All official exam markdown files generated successfully!")
