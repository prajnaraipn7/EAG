from mcp.server.fastmcp import FastMCP, Image
from mcp.server.fastmcp.prompts import base
from mcp.types import TextContent
from mcp import types
from PIL import Image as PILImage
import math
import sys
import subprocess
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

load_dotenv()

# instantiate an MCP server client
mcp = FastMCP("Calculator")

# DEFINE TOOLS

#addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    print("CALLED: add(a: int, b: int) -> int:")
    return int(a + b)

@mcp.tool()
def add_list(l: list) -> int:
    """Add all numbers in a list"""
    print("CALLED: add(l: list) -> int:")
    return sum(l)

# subtraction tool
@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Subtract two numbers"""
    print("CALLED: subtract(a: int, b: int) -> int:")
    return int(a - b)

# multiplication tool
@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    print("CALLED: multiply(a: int, b: int) -> int:")
    return int(a * b)

#  division tool
@mcp.tool() 
def divide(a: int, b: int) -> float:
    """Divide two numbers"""
    print("CALLED: divide(a: int, b: int) -> float:")
    return float(a / b)

# power tool
@mcp.tool()
def power(a: int, b: int) -> int:
    """Power of two numbers"""
    print("CALLED: power(a: int, b: int) -> int:")
    return int(a ** b)

# square root tool
@mcp.tool()
def sqrt(a: int) -> float:
    """Square root of a number"""
    print("CALLED: sqrt(a: int) -> float:")
    return float(a ** 0.5)

# cube root tool
@mcp.tool()
def cbrt(a: int) -> float:
    """Cube root of a number"""
    print("CALLED: cbrt(a: int) -> float:")
    return float(a ** (1/3))

# factorial tool
@mcp.tool()
def factorial(a: int) -> int:
    """factorial of a number"""
    print("CALLED: factorial(a: int) -> int:")
    return int(math.factorial(a))

# log tool
@mcp.tool()
def log(a: int) -> float:
    """log of a number"""
    print("CALLED: log(a: int) -> float:")
    return float(math.log(a))

# remainder tool
@mcp.tool()
def remainder(a: int, b: int) -> int:
    """remainder of two numbers divison"""
    print("CALLED: remainder(a: int, b: int) -> int:")
    return int(a % b)

# sin tool
@mcp.tool()
def sin(a: int) -> float:
    """sin of a number"""
    print("CALLED: sin(a: int) -> float:")
    return float(math.sin(a))

# cos tool
@mcp.tool()
def cos(a: int) -> float:
    """cos of a number"""
    print("CALLED: cos(a: int) -> float:")
    return float(math.cos(a))

# tan tool
@mcp.tool()
def tan(a: int) -> float:
    """tan of a number"""
    print("CALLED: tan(a: int) -> float:")
    return float(math.tan(a))

# mine tool
@mcp.tool()
def mine(a: int, b: int) -> int:
    """special mining tool"""
    print("CALLED: mine(a: int, b: int) -> int:")
    return int(a - b - b)

@mcp.tool()
def create_thumbnail(image_path: str) -> Image:
    """Create a thumbnail from an image"""
    print("CALLED: create_thumbnail(image_path: str) -> Image:")
    img = PILImage.open(image_path)
    img.thumbnail((100, 100))
    return Image(data=img.tobytes(), format="png")

@mcp.tool()
def strings_to_chars_to_int(string: str) -> list[int]:
    """Return the ASCII values of the characters in a word"""
    print("CALLED: strings_to_chars_to_int(string: str) -> list[int]:")
    return [int(ord(char)) for char in string]

@mcp.tool()
def int_list_to_exponential_sum(int_list: list) -> float:
    """Return sum of exponentials of numbers in a list"""
    print("CALLED: int_list_to_exponential_sum(int_list: list) -> float:")
    return sum(math.exp(i) for i in int_list)

@mcp.tool()
def fibonacci_numbers(n: int) -> list:
    """Return the first n Fibonacci Numbers"""
    print("CALLED: fibonacci_numbers(n: int) -> list:")
    if n <= 0:
        return []
    fib_sequence = [0, 1]
    for _ in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]
    
@mcp.tool()
async def open_keynote() -> dict:
    """Open Keynote maximized on secondary monitor using AppleScript"""
    try:
        # Simpler AppleScript that doesn't require accessibility permissions
        apple_script = """
        tell application "Keynote"
            activate
            delay 1
            # Create a new presentation if none exists
            if (count of documents) is 0 then
                make new document
            end if
            # Make sure at least one window exists
            if (count of windows) is 0 then
                make new document
            end if
        end tell
        """
        
        subprocess.run(['osascript', '-e', apple_script], check=True)
        
        return {
            "content": [
                TextContent(
                    type="text",
                    text="Keynote opened successfully. Note: To enable full-screen mode, please grant Accessibility permissions to your terminal/IDE in System Preferences → Security & Privacy → Privacy → Accessibility"
                )
            ]
        }
    except Exception as e:
        return {
            "content": [
                TextContent(
                    type="text",
                    text=f"Error opening Keynote: {str(e)}\nTo enable full functionality, grant Accessibility permissions to your terminal/IDE"
                )
            ]
        }

# @mcp.tool()
# async def clear_keynote_slide() -> dict:
#     """Clear all contents from the current Keynote slide using AppleScript"""
#     try:
#         apple_script = """
#         tell application "Keynote"
#             activate
#             delay 1
            
#             -- Make sure we have a document
#             if not (exists document 1) then
#                 make new document
#             end if
            
#             tell front document
#                 -- Delete all slides first
#                 if (count of slides) > 0 then
#                     delete every slide
#                 end if
                
#                 -- Create new blank slide
#                 make new slide with properties {base slide:master slide "Blank"}
                
#                 -- Make sure we're showing the new slide
#                 show slide 1
#                 delay 0.5
#             end tell
            
#             -- Force update
#             activate
#         end tell
#         """
        
#         print("Executing clear slide command...")
#         result = subprocess.run(['osascript', '-e', apple_script], 
#                               capture_output=True, 
#                               text=True, 
#                               check=True)
        
#         print(f"Clear slide result: {result.stdout}")
        
#         return TextContent(
#             type="text",
#             text="Slide cleared and reset"
#         )
            
#     except subprocess.CalledProcessError as e:
#         error_msg = f"Error: {e.stderr}"
#         print(f"Detailed Error: {error_msg}")
#         return TextContent(
#             type="text",
#             text=f"Error clearing slide: {error_msg}"
#         )
@mcp.tool()
async def clear_keynote_slide() -> dict:
    """Clear all contents from the current Keynote slide using AppleScript"""
    try:
        apple_script = """
        tell application "Keynote"
            if not running then
                return "Keynote is not running"
            end if
            
            tell front document
                -- Store current slide index
                set currentIndex to slide number of current slide
                
                -- Delete the current slide
                delete slide currentIndex
                
                -- Create a new blank slide at the same position
                make new slide at slide currentIndex with properties {base slide:master slide "Blank"}
                
                -- Make it the current slide
                show slide currentIndex
                
            end tell
            
            return "Successfully cleared current slide"
        end tell
        """
        
        result = subprocess.run(['osascript', '-e', apple_script], 
                              capture_output=True, 
                              text=True, 
                              check=True)
        
        success_msg = result.stdout.strip()
        if success_msg:
            return {
                "content": [
                    TextContent(
                        type="text",
                        text=success_msg
                    )
                ]
            }
        else:
            return {
                "content": [
                    TextContent(
                        type="text",
                        text="Slide contents cleared successfully"
                    )
                ]
            }
            
    except subprocess.CalledProcessError as e:
        error_msg = e.stderr.strip() if e.stderr else str(e)
        return {
            "content": [
                TextContent(
                    type="text",
                    text=f"Error clearing slide: {error_msg}"
                )
            ]
        }
@mcp.tool()
async def keep_one_slide() -> dict:
    """Keep only one slide in the Keynote presentation, deleting all others"""
    try:
        apple_script = """
        tell application "Keynote"
            if not running then
                return "Keynote is not running"
            end if
            
            tell front document
                -- Count total slides
                set slideCount to count of slides
                
                if slideCount = 0 then
                    -- If no slides exist, create one
                    make new slide
                    return "Created new slide"
                else if slideCount = 1 then
                    return "Already only one slide"
                else
                    -- Keep first slide, delete the rest
                    repeat with i from slideCount to 2 by -1
                        delete slide i
                    end repeat
                    
                    -- Make sure we're showing the remaining slide
                    show slide 1
                    
                    return "Removed extra slides, kept only one"
                end if
                
                save
            end tell
        end tell
        """
        
        result = subprocess.run(['osascript', '-e', apple_script], 
                              capture_output=True, 
                              text=True, 
                              check=True)
        
        return {
            "content": [
                TextContent(
                    type="text",
                    text=result.stdout.strip() or "Successfully kept only one slide"
                )
            ]
        }
            
    except subprocess.CalledProcessError as e:
        error_msg = e.stderr.strip() if e.stderr else str(e)
        return {
            "content": [
                TextContent(
                    type="text",
                    text=f"Error managing slides: {error_msg}"
                )
            ]
        }
    

@mcp.tool()
async def draw_keynote_rectangle() -> dict:
    """Draw a rectangle in the current Keynote slide"""
    try:
        apple_script = """
        tell application "Keynote"
            activate
            delay 0.5
        end tell
        
        tell application "System Events"
            tell process "Keynote"
                -- Use Insert menu instead of toolbar
                click menu item "Shape" of menu "Insert" of menu bar 1
                delay 0.5
                click menu item "Rectangle" of menu 1 of menu item "Shape" of menu "Insert" of menu bar 1
                
                -- Click to place the shape
                -- The size of shape should be 1000x1000
                
                key code 36
            end tell
        end tell
        
        return "Rectangle drawing process completed"
        """
        
        print("Attempting to draw rectangle...")
        result = subprocess.run(['osascript', '-e', apple_script], 
                              capture_output=True, 
                              text=True, 
                              check=True)
        
        print(f"AppleScript Output: {result.stdout}")
        return {
            "content": [
                TextContent(
                    type="text",
                    text=f"Rectangle drawing completed. Output: {result.stdout}"
                )
            ]
        }
            
    except subprocess.CalledProcessError as e:
        error_msg = f"Error: {e.stderr}"
        print(f"Detailed Error: {error_msg}")
        return {
            "content": [
                TextContent(
                    type="text",
                    text=f"Error drawing rectangle: {error_msg}"
                )
            ]
        }


    
@mcp.tool()
async def write_in_rectangle(text: str = "Hello in Rectangle") -> dict:
    """Write text inside the newly drawn rectangle"""
    try:
        apple_script = f"""
        tell application "Keynote"
            activate
            delay 1
        end tell
        
        tell application "System Events"
            tell process "Keynote"
                -- Click in the middle of the rectangle to select it
                click at {{1200, 800}}
                delay 0.5
                
                -- Double click to enter text editing mode
                click at {{1200, 800}}
                delay 0.2
                click at {{1200, 800}}
                delay 1
                
                -- Type the text
                keystroke "{text}"
                delay 0.5
                
                -- Press Return to finish editing
                keystroke return
            end tell
        end tell
        """
        
        print(f"Writing text in rectangle: {text}")
        result = subprocess.run(['osascript', '-e', apple_script], 
                              capture_output=True, 
                              text=True, 
                              check=True)
        
        return {
            "content": [
                TextContent(
                    type="text",
                    text="Text added to rectangle"
                )
            ]
        }
            
    except subprocess.CalledProcessError as e:
        error_msg = f"Error: {e.stderr}"
        print(f"Detailed Error: {error_msg}")
        return {
            "content": [
                TextContent(
                    type="text",
                    text=f"Error writing text: {error_msg}"
                )
            ]
        }
    
@mcp.tool()
async def send_result_email(result: float, recipient_email: str) -> dict:
    """Send the calculation result via email"""
    try:
        # Get email configuration from environment variables
        smtp_server = os.getenv("SMTP_SERVER")
        smtp_port = int(os.getenv("SMTP_PORT", "587"))
        sender_email = os.getenv("SENDER_EMAIL")
        password = os.getenv("SENDER_PASSWORD")

        # Verify all required credentials are present
        if not all([smtp_server, smtp_port, sender_email, password]):
            raise ValueError("Missing email configuration in .env file")

        # Create message
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = recipient_email
        message["Subject"] = "Fibonacci Exponential Sum Result"
        
        # Email body with more detailed information
        body = f"""
        Hello,
        
        Here are your calculation results:
        
        Fibonacci Sequence Result
        ------------------------
        Exponential Sum: {result}
        
        This email was automatically generated by your Python script.
        
        Best regards,
        Your Python Script
        """
        
        message.attach(MIMEText(body, "plain"))
        
        # Create SMTP session with better error handling
        try:
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                print(f"Connecting to {smtp_server}:{smtp_port}...")
                server.starttls()
                print("Logging in...")
                server.login(sender_email, password)
                print("Sending email...")
                text = message.as_string()
                server.sendmail(sender_email, recipient_email, text)
                print("Email sent successfully!")
        
        except smtplib.SMTPAuthenticationError:
            raise Exception("Email authentication failed. Check your email and password in .env file")
        except smtplib.SMTPException as e:
            raise Exception(f"SMTP error occurred: {str(e)}")
        
        return {
            "content": [
                TextContent(
                    type="text",
                    text=f"Email sent successfully to {recipient_email}"
                )
            ]
        }
            
    except Exception as e:
        error_msg = str(e)
        print(f"Error sending email: {error_msg}")
        return {
            "content": [
                TextContent(
                    type="text",
                    text=f"Error sending email: {error_msg}"
                )
            ]
        }
    
async def run_test():
    """Run a test sequence"""
    print("Running test sequence...")
    try:
        print("Opening Keynote...")
        await open_keynote()
        import time
        time.sleep(2)
        await clear_keynote_slide()
        time.sleep(1)
        await keep_one_slide()
        time.sleep(1)
        await draw_keynote_rectangle()
        time.sleep(1)
        
        # Get Fibonacci numbers and format them
        fib_nums = fibonacci_numbers(5)
        exponential_sum = int_list_to_exponential_sum(fib_nums)
        
        # Format the exponential sum for display
        formatted_result = f"Exponential Sum: {exponential_sum:.2f}"
        
        # Write to rectangle
        await write_in_rectangle(formatted_result)
        time.sleep(1)
        
        # Send email
        recipient_email = "prajnaraipn@gmail.com"
        print(f"Sending result to {recipient_email}...")
        await send_result_email(exponential_sum, recipient_email)
        
        print("Test sequence completed.")
    except Exception as e:
        print(f"Error during test: {str(e)}")

if __name__ == "__main__":
    print("STARTING")
    if len(sys.argv) > 1:
        if sys.argv[1] == "dev":
            mcp.run()
        elif sys.argv[1] == "test":
            import asyncio
            asyncio.run(run_test())
    else:
        mcp.run(transport="stdio")
