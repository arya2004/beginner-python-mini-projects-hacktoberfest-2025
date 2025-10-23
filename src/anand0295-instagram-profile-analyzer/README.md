# 📱 Instagram Profile Analyzer

A beginner-friendly Python application that automatically fetches and analyzes Instagram profile information using the `instaloader` library.

## ✨ Features

- 🔍 **Automatic Profile Analysis** - Comprehensive profile statistics
- 👤 **Profile Information** - Username, full name, bio, follower count
- 📊 **Account Insights** - Verification status, account type, engagement ratios
- 📸 **Profile Picture Download** - Automatically downloads and opens profile pictures
- 📋 **Recent Posts Analysis** - Analyzes latest 5 posts with likes and comments
- 🌐 **Cross-Platform** - Works on Windows, macOS, and Linux

## 🚀 How to Run

### Prerequisites
- Python 3.7 or higher
- Internet connection

### Installation & Usage

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application**
   ```bash
   python main.py
   ```

3. **Enter Instagram username** (without @ symbol)
   ```
   Enter Instagram username (or 'quit' to exit): cristiano
   ```

4. **View Results** - The program will automatically:
   - Fetch complete profile information
   - Display comprehensive statistics
   - Download and open profile picture
   - Analyze recent posts

## 📊 Sample Output

```
==================================================
📱 INSTAGRAM PROFILE INFO
==================================================
👤 Username: @cristiano
📝 Full Name: Cristiano Ronaldo
🆔 User ID: 173560420
📊 Status: ✅ Verified | 🌐 Public

📈 STATISTICS:
   👥 Followers: 615,000,000
   ➡️  Following: 560
   📸 Posts: 3,400
   📊 Following/Followers Ratio: 0.001

📝 Bio:
   SIUUUbscribe on YouTube

🔗 Website: https://www.youtube.com/c/cristiano
```

## 🛠️ Technical Details

- **Language**: Python 3.7+
- **Main Library**: `instaloader` - Instagram data extraction
- **Features**: Profile analysis, image handling, post analytics
- **Compatibility**: Windows, macOS, Linux

## ⚠️ Important Notes

- Works best with **public Instagram profiles**
- Instagram may limit requests if too many are made quickly
- Use responsibly and respect Instagram's Terms of Service
- For educational and research purposes only

## 🤝 Contributing

This project is part of **Hacktoberfest 2025**! Contributions are welcome:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

---

**Made with ❤️ for Hacktoberfest 2025**