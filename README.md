# Deliverable D1 — Trento Energy Portfolio Optimizer (TEPO)

Repository ufficiale del **Deliverable D1** per il progetto **TEPO** (*Trento Energy Portfolio Optimizer*), sviluppato nell'ambito dell'insegnamento di **Ingegneria del Software** (A.A. 2026/2027) presso l'**Università degli Studi di Trento** in cooperazione con l'iniziativa *"100 progetti per il Comune di Trento"*.

- **Codice sorgente del software:** [https://github.com/T-E-P-O/TEPO](https://github.com/T-E-P-O/TEPO)
- **Demo online (Render):** [https://tepo.onrender.com](https://tepo.onrender.com)
- **Team di sviluppo:**
  - Mirco Negri
  - Gabriele Duca
  - Riccardo Scheda

---

## Contenuto del Deliverable

Il presente documento costituisce la baseline formale di specifica dei requisiti e della progettazione iniziale di TEPO:

1. **Il Progetto TEPO** (`sections/Il_nostro_progetto.tex`):
   - Visione, contesto per il Comune di Trento, vantaggi e limiti dichiarati.
   - Prospettive di sviluppo futuro e integrazione con flussi dati reali del Comune.
   - **Giustificazione architetturale dello stack tecnologico:** analisi di trade-off didattica e tecnica su Java 21 + Google OR-Tools CP-SAT rispetto a Node.js, PostgreSQL con Flyway rispetto a MongoDB, e React con TypeScript rispetto a JavaScript puro.
2. **Requisiti Funzionali e Non Funzionali** (`sections/RF.tex`, `sections/RNF.tex`):
   - Specifica dei 16 requisiti funzionali e dei vincoli di qualità (accessibilità WCAG 2.1 AA, prestazioni sub-secondo, affidabilità, licenza, usabilità).
3. **Use Cases e Diagrammi UML** (`sections/UD.tex`, `img/src/`):
   - 15 casi d'uso dettagliati con pre-condizioni, flusso primario, estensioni e diagrammi PlantUML.
4. **User Stories** (`sections/US.tex`):
   - 17 User Stories agili conformi al modello INVEST con criteri di accettazione formulati in stile Given-When-Then.
5. **Design Front-end e Mock-up** (`sections/DesignFrontEnd.tex`, `sections/UF.tex`):
   - Specifiche visuali del design system "Strumento Civico" (doppio registro *Relazione* / *Sala operativa*), wireframe e composizioni d'interfaccia.
6. **Tracciabilità e Gestione delle Modifiche** (`sections/Traceability.tex`, `sections/GestioneModifiche.tex`):
   - Matrice completa e bidirezionale RF <-> RNF <-> UC <-> US <-> Componenti <-> Mock-up.

---

## Compilazione locale e Overleaf

### Compilazione locale (LaTeX)
Per compilare il documento PDF a partire dai sorgenti:

```bash
# Tramite latexmk (raccomandato)
latexmk -pdf D1_main.tex

# Oppure tramite pdflatex (due passaggi per la risoluzione dei riferimenti)
pdflatex D1_main.tex
pdflatex D1_main.tex
```

Il documento compilato finale è disponibile direttamente in questo repository nel file [`D1.pdf`](./D1.pdf).

### Sincronizzazione con Overleaf
Il repository è pronto per l'importazione diretta o la sincronizzazione Git con [Overleaf](https://www.overleaf.com):
- Master file: `D1_main.tex`
- Compilatore: `pdfLaTeX`
