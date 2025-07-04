#!/usr/bin/env python3
"""
US Flag ASCII Art Generator
Prints a representation of the United States flag using ASCII characters.
"""

def print_us_flag():
    """Print the US flag as ASCII art."""
    
    # Flag dimensions
    flag_width = 147  # Reduced from 173
    stripe_height = 3  # Each stripe is 3 lines high
    num_stripes = 13
    canton_width = 57  # Remains the same
    canton_height = 7  # Canton spans 7 stripes (rows)
    
    # Colors using ANSI escape codes
    RED = '\033[41m'      # Red background
    WHITE = '\033[47m'    # White background
    BLUE = '\033[44m'     # Blue background
    RESET = '\033[0m'     # Reset colors
    
    # A 9-row star pattern for the canton to represent exactly 50 stars
    # Alternating 6 and 5 stars: 6+5+6+5+6+5+6+5+6 = 50 stars
    # Each star has 2 spaces from its horizontal neighbor
    star_rows = [
        "      ☆        ☆        ☆        ☆        ☆        ☆   ",  # 6 stars
           "        ☆        ☆        ☆        ☆        ☆        ",  # 5 stars  
           "   ☆        ☆        ☆        ☆        ☆        ☆   ",  # 6 stars
           "        ☆        ☆        ☆        ☆        ☆        ",  # 5 stars
           "   ☆        ☆        ☆        ☆        ☆        ☆   ",  # 6 stars
           "        ☆        ☆        ☆        ☆        ☆        ",  # 5 stars
           "   ☆        ☆        ☆        ☆        ☆        ☆   ",  # 6 stars
           "        ☆        ☆        ☆        ☆        ☆        ",  # 5 stars
           "   ☆        ☆        ☆        ☆        ☆        ☆   ",  # 6 stars
    ]
    
    print("\n" + "="*flag_width)
    print("🇺🇸 UNITED STATES FLAG 🇺🇸".center(flag_width))
    print("="*flag_width + "\n")
    
    # Print the flag
    for i in range(num_stripes):
        stripe_color = RED if i % 2 == 0 else WHITE
        
        for j in range(stripe_height):
            if i < canton_height:
                # Canton area (first 7 stripes)
                # An empty blue line is added at the top, so stars are on the second line.
                if j == 1: # Stars are now on the second line of the stripe
                    star_line = star_rows[i]
                    canton_content = star_line.center(canton_width)
                else:
                    canton_content = " " * canton_width

                remaining_width = flag_width - canton_width
                
                print(BLUE + canton_content + RESET + stripe_color + " " * remaining_width + RESET)
            else:
                # Stripes below the canton
                print(stripe_color + " " * flag_width + RESET)

    print("\n" + "="*flag_width)
    print("Happy Independence Day! 🎆".center(flag_width))
    print("="*flag_width + "\n")

def print_simple_flag():
    """Print a simpler version without ANSI colors for better compatibility."""
    
    print("\n" + "="*60)
    print("🇺🇸 UNITED STATES FLAG (Simple) 🇺🇸".center(60))
    print("="*60 + "\n")
    
    # Simple ASCII version with correct 50 stars, centered
    flag = [
        "  *   *   *   *   *   *  ::::::::::::::::::::::::::::::::",
        "    *   *   *   *   *    ::::::::::::::::::::::::::::::::",
        "  *   *   *   *   *   *  ::::::::::::::::::::::::::::::::",
        "    *   *   *   *   *    ::::::::::::::::::::::::::::::::",
        "  *   *   *   *   *   *  ::::::::::::::::::::::::::::::::",
        "    *   *   *   *   *    ::::::::::::::::::::::::::::::::",
        "  *   *   *   *   *   *  ::::::::::::::::::::::::::::::::",
        "    *   *   *   *   *    ::::::::::::::::::::::::::::::::",
        "  *   *   *   *   *   *  ::::::::::::::::::::::::::::::::",
        "============================================================",
        "------------------------------------------------------------",
        "============================================================",
        "------------------------------------------------------------",
        "============================================================",
        "------------------------------------------------------------",
    ]
    
    for line in flag:
        print(line)
    
    print("\n" + "="*60)
    print("Stars (*) & colons (:) = White, Equals (=) & hyphens (-) = Red".center(60))
    print("="*60 + "\n")

if __name__ == "__main__":
    # Print both versions
    print_us_flag()
    print_simple_flag()