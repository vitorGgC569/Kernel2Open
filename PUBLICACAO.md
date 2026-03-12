# Guia de Publicação no PyPI (Python Package Index)

Este guia explica como empacotar e publicar a biblioteca **Universal Heterogeneous Kernel (UHK)** no repositório oficial do Python (PyPI), tornando-a instalável via `pip install uhk-kernel` para qualquer usuário.

## 1. Pré-requisitos

Certifique-se de ter as ferramentas de build instaladas no seu ambiente Python:

```bash
pip install --upgrade pip build twine
```

Você também precisará de uma conta no [PyPI.org](https://pypi.org/).

---

## 2. Preparar o Pacote

O projeto já está configurado (`setup.py` e `MANIFEST.in`). Agora, vamos gerar os arquivos de distribuição (Source Tarball e Wheel).

Na raiz do projeto, execute:

```bash
python3 -m build
```

Isso criará uma pasta `dist/` contendo dois arquivos:
*   `uhk-kernel-1.0.0.tar.gz` (Código fonte)
*   `uhk_kernel-1.0.0-cp3X-cp3X-linux_x86_64.whl` (Binário compilado, se aplicável)

> **Nota:** Como este projeto contém extensões C++, o arquivo `.whl` gerado localmente será específico para a sua plataforma (ex: Linux x86_64). O arquivo `.tar.gz` é genérico e permitirá que outros compilem na instalação.

---

## 3. Testar o Pacote (Opcional, mas Recomendado)

Antes de publicar no PyPI oficial, você pode testar no TestPyPI:

```bash
python3 -m twine upload --repository testpypi dist/*
```

Para instalar do TestPyPI:
```bash
pip install --index-url https://test.pypi.org/simple/ --no-deps uhk-kernel
```

---

## 4. Publicar no PyPI

Se tudo estiver correto, envie para o repositório oficial:

```bash
python3 -m twine upload dist/*
```

Você será solicitado a inserir seu **Username** (`__token__`) e **Password** (seu API Token do PyPI, que deve ser gerado nas configurações da sua conta no site).

---

## 5. Como os usuários vão instalar?

Após a publicação bem-sucedida, qualquer pessoa no mundo poderá instalar sua biblioteca com um único comando:

```bash
pip install uhk-kernel
```

Isso baixará automaticamente as dependências (`numpy`, `brainflow`, `qiskit`, etc.) e compilará o módulo C++ na máquina do usuário.

---

## 6. Dicas Extras

*   **Atualização de Versão:** Se você fizer alterações no código, lembre-se de editar o arquivo `setup.py` e incrementar a versão (ex: `1.0.0` -> `1.0.1`) antes de publicar novamente.
*   **Compilação Cruzada:** Para fornecer binários pré-compilados (Wheels) para Windows, Mac e Linux sem que o usuário precise de compiladores C++, recomenda-se usar o **GitHub Actions** com `cibuildwheel`.
