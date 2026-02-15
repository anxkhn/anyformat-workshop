## Troubleshooting

Common issues and solutions for anyformat-workshop.

### ffmpeg not found

**Error**: `ffmpeg: command not found` or `FileNotFoundError: [Errno 2] No such file or directory: 'ffmpeg'`

**Solution**:
1. Install ffmpeg:
   - **macOS**: `brew install ffmpeg`
   - **Ubuntu/Debian**: `sudo apt install ffmpeg`
   - **Windows**: Download from [ffmpeg.org](https://ffmpeg.org/download.html) and add to PATH

2. Verify installation:
   ```bash
   ffmpeg -version
   ```

3. If installed but not found, ensure it's in your system PATH.

---

### Permission denied errors

**Error**: `PermissionError: [Errno 13] Permission denied`

**Solution**:
1. Check file permissions:
   ```bash
   ls -la /path/to/file
   ```

2. Fix permissions:
   ```bash
   chmod +r /path/to/input/file
   chmod +w /path/to/output/directory
   ```

3. On Linux/macOS, avoid using sudo with pip. Use virtual environments instead:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   # or
   venv\Scripts\activate  # Windows
   pip install -e .
   ```

---

### Invalid format errors

**Error**: `Invalid format: .xyz is not supported` or `Error: Unsupported file format`

**Solution**:
1. Check supported formats:
   ```bash
   anyformat info --formats
   ```

2. Verify file extension matches actual content:
   ```bash
   file video.mp4
   ```

3. Convert to a supported format first using ffmpeg:
   ```bash
   ffmpeg -i input.xyz output.mp4
   ```

4. Supported formats include: MP4, AVI, MOV, MKV, MP3, WAV, FLAC, JPEG, PNG, WebP

---

### Python version errors

**Error**: `Python 3.13 or higher is required` or `SyntaxError` / `ImportError`

**Solution**:
1. Check your Python version:
   ```bash
   python --version
   # or
   python3 --version
   ```

2. Install Python 3.13+:
   - **macOS**: `brew install python@3.13`
   - **Ubuntu**: 
     ```bash
     sudo apt update
     sudo apt install python3.13 python3.13-venv
     ```
   - **Windows**: Download from [python.org](https://python.org)

3. Use the correct Python version:
   ```bash
   python3.13 -m pip install -e .
   ```

4. Consider using pyenv for version management:
   ```bash
   pyenv install 3.13
   pyenv local 3.13
   ```

---

### Module not found errors

**Error**: `ModuleNotFoundError: No module named 'anyformat'`

**Solution**:
1. Ensure you installed in editable mode:
   ```bash
   pip install -e .
   ```

2. Verify you're in the project root directory when installing.

3. Check your Python environment is activated:
   ```bash
   which python  # Should show your venv path
   ```

---

### Conversion fails silently

**Error**: Command completes but output file is empty or corrupted

**Solution**:
1. Check input file is valid:
   ```bash
   anyformat info input.mp4
   ```

2. Try with verbose output:
   ```bash
   anyformat convert input.mp4 output.mp4 --verbose
   ```

3. Check disk space:
   ```bash
   df -h
   ```

4. Verify ffmpeg is properly installed:
   ```bash
   ffmpeg -version
   ```

---

### Still having issues?

1. Check existing [GitHub Issues](../../issues) for similar problems
2. Open a new issue with:
   - Full error message
   - Command you ran
   - Your OS and Python version
   - Steps to reproduce
