Para iniciar, mude para o venv `app`:

```powershell
app\Scripts\Activate.ps1
```

Depois execute o script inicial

```python
py init.py
```

Salvar dependências no `requirements.txt`:

```powershell
pip freeze | Set-Content -Path requirements.txt -Encoding Utf8
```
