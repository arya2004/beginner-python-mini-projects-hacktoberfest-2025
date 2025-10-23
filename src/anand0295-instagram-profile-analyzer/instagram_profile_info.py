"""
Instagram Profile Analyzer
==========================

A powerful yet beginner-friendly Python application that automatically fetches 
and analyzes Instagram profile information using the reliable instaloader library.

Features:
- Automatic profile analysis with comprehensive statistics
- Profile picture download and instant opening
- Recent posts analysis with engagement metrics
- Cross-platform compatibility (Windows, macOS, Linux)
- Clean, professional output formatting

Author: Anand
Version: 1.0.0
License: MIT

Requirements:
    pip install instaloader

Usage:
    python main.py
"""

import instaloader
from datetime import datetime
import sys

class InstagramProfileFetcher:
    """Simple Instagram profile fetcher using instaloader"""
    
    def __init__(self):
        # Create instaloader instance
        self.loader = instaloader.Instaloader()
        
        # Configure instaloader settings for better reliability
        self.loader.context._session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    def get_profile_info(self, username):
        """
        Get profile information for a given username
        Returns profile object or None if error occurs
        """
        try:
            # Remove @ symbol if present
            username = username.replace('@', '').strip()
            
            print(f"🔍 Fetching profile info for @{username}...")
            
            # Get profile using instaloader
            profile = instaloader.Profile.from_username(self.loader.context, username)
            
            return profile
            
        except instaloader.exceptions.ProfileNotExistsException:
            print(f"❌ Profile @{username} does not exist!")
            return None
        except instaloader.exceptions.PrivateProfileNotFollowedException:
            print(f"🔒 Profile @{username} is private and you don't follow them!")
            return None
        except Exception as e:
            print(f"❌ Error fetching profile: {e}")
            return None
    
    def display_profile_info(self, profile):
        """Display profile information in a nice format"""
        
        print("\n" + "="*50)
        print(f"📱 INSTAGRAM PROFILE INFO")
        print("="*50)
        
        # Basic Information
        print(f"👤 Username: @{profile.username}")
        print(f"📝 Full Name: {profile.full_name}")
        print(f"🆔 User ID: {profile.userid}")
        
        # Account Status
        status = []
        if profile.is_verified:
            status.append("✅ Verified")
        if profile.is_private:
            status.append("🔒 Private")
        else:
            status.append("🌐 Public")
        if profile.is_business_account:
            status.append("💼 Business")
        
        print(f"📊 Status: {' | '.join(status)}")
        
        # Statistics
        print(f"\n📈 STATISTICS:")
        print(f"   👥 Followers: {profile.followers:,}")
        print(f"   ➡️  Following: {profile.followees:,}")
        print(f"   📸 Posts: {profile.mediacount:,}")
        
        # Calculate engagement ratio (rough estimate)
        if profile.followers > 0:
            following_ratio = profile.followees / profile.followers
            print(f"   📊 Following/Followers Ratio: {following_ratio:.3f}")
        
        # Bio and External URL
        if profile.biography:
            print(f"\n📝 Bio:")
            # Split bio into lines for better formatting
            bio_lines = profile.biography.split('\n')
            for line in bio_lines:
                if line.strip():  # Only print non-empty lines
                    print(f"   {line}")
        
        if profile.external_url:
            print(f"\n🔗 Website: {profile.external_url}")
        
        # Business Category (if available)
        if hasattr(profile, 'business_category_name') and profile.business_category_name:
            print(f"🏷️  Business Category: {profile.business_category_name}")
        
        print("="*50)
    
    def save_and_open_profile_picture(self, profile):
        """Download, save and open profile picture"""
        try:
            print(f"\n📸 Downloading and opening profile picture for @{profile.username}...")
            
            # Download profile picture
            self.loader.download_profile(profile.username, profile_pic_only=True)
            
            # Try to open the profile picture
            import os
            import subprocess
            import platform
            import glob
            
            # Look for the downloaded profile picture with different possible extensions
            possible_paths = [
                f"{profile.username}/{profile.username}.jpg",
                f"{profile.username}/{profile.username}.jpeg",
                f"{profile.username}/{profile.username}.png",
                f"{profile.username}/{profile.username}.webp"
            ]
            
            # Also try to find any image file in the username directory
            username_dir = profile.username
            if os.path.exists(username_dir):
                image_files = glob.glob(f"{username_dir}/*.jpg") + \
                             glob.glob(f"{username_dir}/*.jpeg") + \
                             glob.glob(f"{username_dir}/*.png") + \
                             glob.glob(f"{username_dir}/*.webp")
                possible_paths.extend(image_files)
            
            pic_path = None
            for path in possible_paths:
                if os.path.exists(path):
                    pic_path = path
                    break
            
            if pic_path:
                print(f"📁 Found profile picture at: {pic_path}")
                
                # Get absolute path
                abs_pic_path = os.path.abspath(pic_path)
                
                # Open the image based on the operating system
                try:
                    if platform.system() == "Darwin":  # macOS
                        subprocess.run(["open", abs_pic_path], check=True)
                    elif platform.system() == "Windows":  # Windows
                        os.startfile(abs_pic_path)
                    else:  # Linux
                        subprocess.run(["xdg-open", abs_pic_path], check=True)
                    
                    print(f"✅ Profile picture saved and opened!")
                except subprocess.CalledProcessError:
                    print(f"❌ Could not open image automatically")
                    print(f"📁 You can find the image at: {abs_pic_path}")
                except Exception as open_error:
                    print(f"❌ Could not open image: {open_error}")
                    print(f"📁 You can find the image at: {abs_pic_path}")
            else:
                print(f"❌ Could not find downloaded profile picture")
                # List what files were actually downloaded
                if os.path.exists(profile.username):
                    files = os.listdir(profile.username)
                    print(f"📁 Files in {profile.username}/ directory: {files}")
                else:
                    print(f"📁 Directory {profile.username}/ was not created")
            
        except Exception as e:
            print(f"❌ Could not download/open profile picture: {e}")
            import traceback
            print(f"🔍 Debug info: {traceback.format_exc()}")
    
    def get_recent_posts_info(self, profile, num_posts=5):
        """Get information about recent posts"""
        try:
            print(f"\n📸 Getting info about {num_posts} most recent posts...")
            
            posts = []
            count = 0
            
            for post in profile.get_posts():
                if count >= num_posts:
                    break
                
                post_info = {
                    'date': post.date_utc.strftime('%Y-%m-%d %H:%M:%S'),
                    'likes': post.likes,
                    'comments': post.comments,
                    'caption': post.caption[:100] + "..." if post.caption and len(post.caption) > 100 else post.caption,
                    'is_video': post.is_video,
                    'url': f"https://www.instagram.com/p/{post.shortcode}/"
                }
                
                posts.append(post_info)
                count += 1
            
            # Display recent posts info
            print(f"\n📋 RECENT POSTS ({len(posts)} posts):")
            print("-" * 40)
            
            for i, post in enumerate(posts, 1):
                print(f"{i}. Posted: {post['date']}")
                print(f"   ❤️  Likes: {post['likes']:,} | 💬 Comments: {post['comments']:,}")
                if post['is_video']:
                    print(f"   🎥 Video Post")
                else:
                    print(f"   📷 Photo Post")
                if post['caption']:
                    print(f"   📝 Caption: {post['caption']}")
                print(f"   🔗 URL: {post['url']}")
                print()
            
        except Exception as e:
            print(f"❌ Could not fetch recent posts: {e}")


def main():
    """Main program function"""
    print("🎓 Instagram Profile Analyzer")
    print("Using Instaloader Library - Auto Mode")
    print("-" * 50)
    
    # Check if instaloader is installed
    try:
        import instaloader
    except ImportError:
        print("❌ Instaloader not installed!")
        print("Install it with: pip install instaloader")
        sys.exit(1)
    
    # Create fetcher instance
    fetcher = InstagramProfileFetcher()
    
    while True:
        print("\n" + "="*30)
        print("INSTAGRAM PROFILE ANALYZER")
        print("="*30)
        
        username = input("\nEnter Instagram username (or 'quit' to exit): ").strip()
        
        if username.lower() in ['quit', 'exit', 'q']:
            print("👋 Thanks for using the program!")
            break
        
        if not username:
            print("❌ Please enter a valid username!")
            continue
        
        # Get profile information
        profile = fetcher.get_profile_info(username)
        
        if profile:
            # Display basic profile info
            fetcher.display_profile_info(profile)
            
            # Automatically do everything
            print("\n🚀 Auto-analyzing profile (downloading picture + analyzing posts)...")
            
            # Download and open profile picture
            fetcher.save_and_open_profile_picture(profile)
            
            # Analyze recent posts (default 5)
            fetcher.get_recent_posts_info(profile, 5)
        
        # Ask if user wants to analyze another profile
        continue_choice = input("\n🔄 Analyze another profile? (y/n): ").strip().lower()
        if continue_choice not in ['y', 'yes']:
            print("👋 Thanks for using the program!")
            break


if __name__ == "__main__":
    main()