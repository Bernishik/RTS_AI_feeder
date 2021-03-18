# How to launch a project #
All what you need is simply run file `app.py`

If you want to run scraping you should send get request using this url `http://0.0.0.0:5000/`

If you want run `converter`, you should send get request using url `http://0.0.0.0:5000/converter` with text like that:

```
{
    "pdf": ["https://www.nature.com/articles/453028a.pdf"],
    "docx": ["https://pasteur.epa.gov/uploads/10.23719/1500001/LDPE_nanoclay_Highlights_.docx"]
}
```