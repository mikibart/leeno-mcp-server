# LeenO MCP Server

MCP (Model Context Protocol) Server per la gestione di computi metrici estimativi tramite LeenO e LibreOffice.

## Cos'è

Questo server MCP permette a un agente AI (come Claude) di gestire documenti di computo metrico creati con [LeenO](https://leeno.org), l'estensione open source per LibreOffice Calc.

## Funzionalità

### Gestione Documenti
- Creare nuovi documenti LeenO
- Aprire documenti esistenti
- Salvare e chiudere documenti
- Ottenere statistiche e informazioni

### Computo Metrico
- Aggiungere/eliminare voci di lavoro
- Gestire capitoli e sottocapitoli
- Aggiungere righe di misurazione
- Calcolare totali

### Elenco Prezzi
- Cercare prezzi per codice o descrizione
- Aggiungere/modificare/eliminare prezzi
- Importare prezzari regionali

### Contabilità Lavori
- Aggiungere voci di contabilità
- Gestire SAL (Stati Avanzamento Lavori)
- Verificare stato della contabilità

### Export
- Esportare in PDF
- Esportare in CSV
- Esportare in Excel (XLSX)

## Requisiti

- Python 3.10+
- LibreOffice 7.0+
- LeenO extension installata in LibreOffice

## Installazione

```bash
# Clona il repository
cd leeno-mcp-server

# Installa le dipendenze
pip install -e .

# Oppure con pip
pip install leeno-mcp
```

## Utilizzo

### 1. Avvia LibreOffice in modalità headless

**Windows:**
```batch
scripts\start_libreoffice.bat
```

**Linux/Mac:**
```bash
chmod +x scripts/start_libreoffice.sh
./scripts/start_libreoffice.sh
```

Oppure manualmente:
```bash
soffice --headless --accept="socket,host=localhost,port=2002;urp;StarOffice.ComponentContext"
```

### 2. Avvia il server MCP

```bash
leeno-mcp
```

### 3. Configura il tuo client MCP

Aggiungi al file di configurazione del tuo client MCP:

```json
{
  "mcpServers": {
    "leeno": {
      "command": "leeno-mcp"
    }
  }
}
```

## Tool Disponibili

### Documenti
| Tool | Descrizione |
|------|-------------|
| `leeno_document_create` | Crea nuovo documento |
| `leeno_document_open` | Apre documento esistente |
| `leeno_document_save` | Salva documento |
| `leeno_document_close` | Chiude documento |
| `leeno_document_list` | Lista documenti aperti |
| `leeno_document_info` | Info e statistiche |

### Computo
| Tool | Descrizione |
|------|-------------|
| `leeno_computo_add_voce` | Aggiunge voce |
| `leeno_computo_list_voci` | Lista voci |
| `leeno_computo_get_voce` | Dettaglio voce |
| `leeno_computo_delete_voce` | Elimina voce |
| `leeno_computo_add_capitolo` | Aggiunge capitolo |
| `leeno_computo_add_misura` | Aggiunge misura |
| `leeno_computo_get_totale` | Totale computo |
| `leeno_computo_get_struttura` | Struttura completa |

### Prezzi
| Tool | Descrizione |
|------|-------------|
| `leeno_prezzi_search` | Cerca prezzi |
| `leeno_prezzi_get` | Dettaglio prezzo |
| `leeno_prezzi_add` | Aggiunge prezzo |
| `leeno_prezzi_edit` | Modifica prezzo |
| `leeno_prezzi_delete` | Elimina prezzo |
| `leeno_prezzi_list` | Lista prezzi |
| `leeno_prezzi_count` | Conta prezzi |

### Contabilità
| Tool | Descrizione |
|------|-------------|
| `leeno_contab_add_voce` | Aggiunge voce |
| `leeno_contab_list_voci` | Lista voci |
| `leeno_contab_get_sal` | Info SAL |
| `leeno_contab_get_stato` | Stato contabilità |

### Export
| Tool | Descrizione |
|------|-------------|
| `leeno_export_pdf` | Esporta PDF |
| `leeno_export_csv` | Esporta CSV |
| `leeno_export_xlsx` | Esporta Excel |
| `leeno_export_formats` | Formati disponibili |

## Configurazione

Variabili d'ambiente:

| Variabile | Descrizione | Default |
|-----------|-------------|---------|
| `LEENO_UNO_HOST` | Host LibreOffice | localhost |
| `LEENO_UNO_PORT` | Porta LibreOffice | 2002 |
| `LEENO_PATH` | Percorso estensione LeenO | auto-detect |
| `LEENO_LOG_LEVEL` | Livello log | INFO |

## Esempio di utilizzo

```
User: Crea un nuovo computo metrico

AI: [Chiama leeno_document_create]
    Documento creato con ID: doc_a1b2c3d4

User: Aggiungi un capitolo "OPERE MURARIE"

AI: [Chiama leeno_computo_add_capitolo con nome="OPERE MURARIE", livello=1]
    Capitolo aggiunto: CAP_001

User: Cerca nel prezzario "scavo"

AI: [Chiama leeno_prezzi_search con query="scavo"]
    Trovati 15 prezzi:
    - [01.A01.001] Scavo a sezione aperta... mc € 12.50
    - [01.A01.002] Scavo in trincea... mc € 18.00
    ...

User: Aggiungi la prima voce con quantità 100 mc

AI: [Chiama leeno_computo_add_voce con codice="01.A01.001", quantita=100]
    Voce aggiunta: V001, importo € 1,250.00

User: Qual è il totale?

AI: [Chiama leeno_computo_get_totale]
    Totale computo: € 1,250.00
    Sicurezza: € 37.50
    Manodopera: € 375.00
```

## Licenza

MIT License

## Link Utili

- [LeenO](https://leeno.org) - Estensione per LibreOffice
- [Telegram LeenO](https://t.me/leeno_computometrico) - Supporto
- [MCP Protocol](https://modelcontextprotocol.io/) - Model Context Protocol
