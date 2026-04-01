Hey everyone! 👋

Please complete this task by submitting a PR to the repo:
🔗 https://github.com/Ignitzsolutions/genai-se-2026

**Follow these steps:**

**1. Fork the repo**

* Click the **Fork** button (top right)

**2. Clone your fork**

```bash
git clone https://github.com/YOUR-USERNAME/genai-se-2026.git
cd genai-se-2026
```

**3. Create a new branch**

```bash
git checkout -b feature-yourname
```

**4. Add a Python file**

```bash
echo "print('Hello from YOUR NAME')" > yourname.py
```

(or create any `.py` file with your own code)

**5. Add and commit**

```bash
git add .
git commit -m "Added python file - Your Name"
```

**6. Push your branch**

```bash
git push origin feature-yourname
```

**7. Create PR**

* Go to your fork on GitHub
* Click **Compare & pull request**
* Submit the PR 🚀

## Automation Task - Word Count Script

- What it does: reads `automation/sample.txt`, counts words, prints result to console
- Logging: `automation/app.log` gets start/success/failure messages
- Error handling: try/except with exception logging and re-raise
- How to run:

```bash
python automation/word_count_task.py
```

With custom file or log path:

```bash
python automation/word_count_task.py --file automation/sample.txt --log automation/app.log
```
