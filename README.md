# 📦 SISETRWEB Installation Package

> Complete installation package for SISETRWEB trading bot - Python 3.14 compatible

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-blue)](https://www.python.org/downloads/)
[![Windows](https://img.shields.io/badge/Platform-Windows-blue)](https://www.microsoft.com/windows)

---

## 🎯 Overview

This package contains everything you need to install **SISETRWEB** on Windows with Python 3.14 or any other version. It solves all dependency issues and provides automated installation scripts.

### ✨ Key Features

- ✅ **Zero Compilation Issues** - All dependencies are precompiled wheels
- ✅ **Python 3.14 Compatible** - Works with Python 3.11, 3.12, 3.13, 3.14+
- ✅ **Automated Installation** - PowerShell and Batch scripts included
- ✅ **No External Dependencies** - Pure Python technical analysis module
- ✅ **Complete Documentation** - Multiple guides in Spanish and English

---

## 📋 Package Contents

| File | Purpose |
|------|---------|
| **README.md** | This file - English overview |
| **README_INSTALACION.md** | Spanish installation guide |
| **INSTRUCCIONES_URGENTES.md** | Critical instructions (Spanish) |
| **PYTHON_314_NUMBA_FIX.md** | Technical documentation (Spanish) |
| **requirements_final.txt** | Python dependencies (NO numba, NO pandas-ta) |
| **technical_analysis_pure_python.py** | Pure Python technical analysis module |
| **install_now.ps1** | Automated PowerShell installer ⭐ RECOMMENDED |
| **install_final.bat** | Automated Batch installer (alternative) |

---

## 🚀 Quick Start (3 Steps)

### Step 1: Download & Extract
- Download this repository as ZIP
- Extract all files to your SISETRWEB folder

### Step 2: Copy Files
Copy files to the correct locations:

```
C:\xampp\htdocs\sisetrweb\
├── requirements_final.txt              ← Copy here
├── install_now.ps1                     ← Copy here
├── install_final.bat                   ← Copy here
├── src\engines\
│   └── technical_analysis_pure_python.py  ← Copy here
└── ... (other existing files)
```

### Step 3: Run Installer
Open PowerShell in your SISETRWEB folder and run:

```powershell
cd C:\xampp\htdocs\sisetrweb
.\install_now.ps1
```

**The script will automatically:**
- ✅ Clean previous installation
- ✅ Create virtual environment
- ✅ Install all dependencies
- ✅ Copy technical analysis module
- ✅ Verify installation
- ✅ Run diagnostics

**Estimated time: 10-15 minutes**

---

## ⚙️ Installation Methods

### Method 1: PowerShell (RECOMMENDED)
```powershell
.\install_now.ps1
```

### Method 2: Batch Script
```cmd
.\install_final.bat
```

### Method 3: Manual Installation
```bash
# Clean previous installation
rmdir /s /q venv

# Create virtual environment
python -m venv venv

# Activate environment
.\venv\Scripts\activate

# Install dependencies (use requirements_final.txt, NOT requirements.txt)
pip install -r requirements_final.txt --no-cache-dir

# Copy technical analysis module
copy src\engines\technical_analysis_pure_python.py src\engines\technical_analysis.py

# Start the bot
python run_system.bat
```

---

## ✅ Verification

After installation, verify everything works:

```bash
# Activate environment
.\venv\Scripts\activate

# Verify critical modules
python -c "
import pandas
import fastapi
import uvicorn
import apscheduler
print('✅ All modules installed successfully!')
"

# Start the bot
python run_system.bat
```

---

## ⚠️ Important Notes

### DO NOT Use
- ❌ `requirements.txt` (original file with numba/pandas-ta)
- ❌ `requirements_alternative.txt`
- ❌ `requirements_windows_optimized.txt`

### DO Use
- ✅ `requirements_final.txt` (included in this package)

### Why?
The original `requirements.txt` contains:
- `pandas-ta` which depends on `numba`
- `numba` does NOT support Python 3.14
- This causes compilation errors on Windows

This package provides:
- `requirements_final.txt` with NO numba/pandas-ta
- `technical_analysis_pure_python.py` - Pure Python implementation
- All dependencies are precompiled wheels (no compilation needed)

---

## 🔧 Technical Details

### Python Version Support
- ✅ Python 3.11.x
- ✅ Python 3.12.x
- ✅ Python 3.13.x
- ✅ Python 3.14.x (development version)

### Dependencies
All dependencies are precompiled wheels:
- pandas (≥2.1.0)
- numpy (≥1.26.0)
- fastapi (≥0.104.1)
- uvicorn (≥0.24.0)
- MetaTrader5 (5.0.45)
- APScheduler (≥3.10.4)
- python-telegram-bot (≥20.3)
- google-auth-oauthlib (≥1.0.0)
- openpyxl (≥3.1.2)
- And more...

### Technical Analysis Module
The `technical_analysis_pure_python.py` module implements:
- RSI (Relative Strength Index)
- MACD (Moving Average Convergence Divergence)
- Bollinger Bands
- ATR (Average True Range)
- Stochastic Oscillator
- EMA (Exponential Moving Average)
- SMA (Simple Moving Average)
- ADX (Average Directional Index)

All implemented in pure Python without external compilation.

---

## 🆘 Troubleshooting

### Problem: "Could not open requirements file"
**Solution**: Make sure you're in the correct directory and using `requirements_final.txt`

```bash
# Verify file exists
dir requirements_final.txt

# Install from correct file
pip install -r requirements_final.txt --no-cache-dir
```

### Problem: "ModuleNotFoundError: No module named 'numba'"
**Solution**: You're using the wrong requirements file. Use `requirements_final.txt` instead.

```bash
# Clean and reinstall
rmdir /s /q venv
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements_final.txt --no-cache-dir
```

### Problem: Script won't run
**Solution**: Enable script execution in PowerShell

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\install_now.ps1
```

### Problem: Still having issues?
1. Read `INSTRUCCIONES_URGENTES.md`
2. Read `PYTHON_314_NUMBA_FIX.md`
3. Open an issue on GitHub

---

## 📚 Documentation

- **Spanish Installation Guide**: `README_INSTALACION.md`
- **Urgent Instructions (Spanish)**: `INSTRUCCIONES_URGENTES.md`
- **Technical Documentation (Spanish)**: `PYTHON_314_NUMBA_FIX.md`
- **GitHub Repository Setup**: See main SISETRWEB repository

---

## 🤝 Support

For issues or questions:
1. Check the documentation files included
2. Open an issue on the main SISETRWEB repository:
   https://github.com/toledomendizabal/sisetrweb/issues
3. Include error messages and steps taken

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 👨‍💻 Author

**SISETRWEB Development Team**

- **Repository**: https://github.com/toledomendizabal/sisetrweb
- **Installation Package**: https://github.com/toledomendizabal/sisetrweb-installation
- **Web Info**: https://github.com/toledomendizabal/sisetrweb-info-page

---

## 📊 Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | May 2026 | Initial release - Complete installation package |

---

## 🎯 Roadmap

- [ ] Add GitHub Actions for automated testing
- [ ] Create Docker container for easy deployment
- [ ] Add Linux/Mac installation support
- [ ] Create video tutorial

---

**Last Updated**: May 2026  
**Compatibility**: Windows 10/11 with Python 3.11+  
**Status**: ✅ Production Ready
