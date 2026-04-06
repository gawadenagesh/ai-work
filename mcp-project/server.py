import sqlite3
from mcp.server.fastmcp import FastMCP

# Create a new MCP server instance
mcp = FastMCP("sqlite-mcp")

# read data from SQLLite
@mcp.tool()     
def get_data(query: str) -> str:
    """Read data from SQLLite"""
    conn = sqlite3.connect("demo.db")
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()
    return rows 

# write data to SQLLite
@mcp.tool()
def write_data(query: str) -> str:
    """Write data to SQLLite"""
    conn = sqlite3.connect("demo.db")
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    conn.close()
    return "Data written successfully"      

# Run the server
if __name__ == "__main__":
    mcp.run()