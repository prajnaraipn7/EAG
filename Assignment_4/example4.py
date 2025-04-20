import sys
import subprocess
from dotenv import load_dotenv
from mcp import types
from mcp.server.fastmcp import FastMCP
from mcp.types import TextContent
from mcp.server.fastmcp.prompts import base

mcp = FastMCP("MacKeynoteAgent")

# Open Keynote
@mcp.tool()
def open_keynote() -> dict:
    """Open Keynote app and create a new document."""
    print("Attempting to open Keynote...")
    try:
        script = '''
        tell application "Keynote"
            activate
            if (count of documents) is 0 then
                make new document
            end if
            delay 1
        end tell
        '''
        subprocess.run(["osascript", "-e", script])
        return {
            "content": [
                TextContent(type="text", text="Keynote opened successfully with new document.")
            ]
        }
    except Exception as e:
        return {
            "content": [
                TextContent(type="text", text=f"Error opening Keynote: {str(e)}")
            ]
        }

@mcp.tool()
def clear_slide() -> dict:
    """Clear absolutely everything from the slide in Keynote."""
    print("Attempting to clear entire presentation and metadata")
    try:
        script = '''
        tell application "Keynote"
            tell front document
                delete every slide
                make new slide
            end tell
        end tell
        '''
        subprocess.run(["osascript", "-e", script], shell=True)
        return {
            "content": [
                TextContent(type="text", text="Slide cleared successfully")
            ]
        }
    except Exception as e:
        return {
            "content": [
                TextContent(type="text", text=f"Error clearing slide: {str(e)}")
            ]
        }

@mcp.tool()
def draw_rectangle() -> dict:
    """Draw a rectangle with blue border and white fill in Keynote"""
    print("Attempting to draw rectangle...")
    try:
        script = '''
        tell application "Keynote"
            tell front document
                tell slide 1
                    make new shape
                    tell last shape
                        set width to 500
                        set height to 500
                        set position to {700, 300}
                    end tell
                end tell
            end tell
        end tell
        '''
        subprocess.run(["osascript", "-e", script], shell=True)
        return {
            "content": [
                TextContent(type="text", text="Rectangle drawn successfully")
            ]
        }
    except Exception as e:
        return {
            "content": [
                TextContent(type="text", text=f"Error drawing rectangle: {str(e)}")
            ]
        }

def run_test():
    """Run a test sequence"""
    print("Running test sequence...")
    open_keynote()
    import time
    time.sleep(2)
    clear_slide()  # Wait for Keynote to open
    draw_rectangle()
    # add_text_to_slide("Hello, this is a test!")
    print("Test sequence completed.")

if __name__ == "__main__":
    print("STARTING")
    if len(sys.argv) > 1:
        if sys.argv[1] == "dev":
            mcp.run()
        elif sys.argv[1] == "test":
            run_test()
    else:
        mcp.run(transport="stdio")