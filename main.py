output.seek(0)
    return output

# Store latest bookings for download
latest_bookings = []

@app.get("/", response_class=HTMLResponse)
async def upload_form(request: Request):
    return templates.TemplateResponse("upload.html", {"request": request})

@app.post("/", response_class=HTMLResponse)
async def upload_file(request: Request, file: UploadFile = Form(...)):
    global latest_bookings
    rows = parse_csv(file)
    bookings = process_bookings(rows)
    # Save to session-like object (simulate with in-memory for now)
    request.state.bookings = bookings
    latest_bookings = bookings
    # Prepare data for template
    result = [(i+1, b[0]) for i, b in enumerate(bookings)]
    # Store CSV in memory for download
    csv_content = generate_csv(bookings).getvalue()
    request.state.csv_content = csv_content
    return templates.TemplateResponse("result.html", {"request": request, "result": result, "csv_ready": True})
    sequence = [{"seq": i+1, "booking_id": b[0]} for i, b in enumerate(bookings)]
    return templates.TemplateResponse("result.html", {"request": request, "sequence": sequence, "csv_ready": True})

@app.get("/result/", response_class=HTMLResponse)
async def result_page(request: Request):
    # This would normally use session or DB; here, just show upload page
    return RedirectResponse("/")

@app.get("/download/", response_class=StreamingResponse)
async def download_csv(request: Request):
    # In a real app, use session or DB; here, just return a sample
    bookings = [("103", ["A2"]), ("101", ["A1", "B1"]), ("120", ["A20", "C2"]), ("102", ["B2", "B3"])]
    output = generate_csv(bookings)
    global latest_bookings
    output = generate_csv(latest_bookings)
    response = StreamingResponse(iter([output.getvalue()]), media_type="text/csv")
    response.headers["Content-Disposition"] = "attachment; filename=boarding_sequence.csv"
    return response 
