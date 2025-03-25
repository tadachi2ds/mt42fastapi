from fastapi import FastAPI, Query

app = FastAPI()

# prev_close の初期化
app.state.prev_close = -1

@app.get("/")
def root():
    return "OK"

@app.get("/reset")
def reset():
    app.state.prev_close = -1
    return ""

@app.get("/ontick")
def ontick(
    symbol: str = Query(...),
    time: str = Query(...),
    open: float = Query(...),
    high: float = Query(...),
    low: float = Query(...),
    close: float = Query(...)
):
    prev_close = app.state.prev_close

    if prev_close == -1:
        prev_close = close

    print(open, high, low, close, prev_close)

    app.state.prev_close = close

    return f"symbol:{symbol}, time:{time}, open:{open}, high:{high}"
    # return "OK"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8080)