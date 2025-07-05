## 🎯 **UPLOAD MANUALE SU GITHUB (5 minuti)**

### **METODO DRAG & DROP:**

1. **🌐 Vai al tuo repository**: `https://github.com/[TUO-USERNAME]/task-manager-app`

2. **📁 Crea struttura cartelle**:
   - Clicca **"Create new file"**
   - Nome file: `backend/server.py`
   - Incolla questo contenuto:
Action: file_editor view /app/backend/server.py --view-range-start 1 --view-range-end 50
Observation: /app/backend/server.py:
1|from fastapi import FastAPI, APIRouter, HTTPException, Query
2|from fastapi.middleware.cors import CORSMiddleware
3|from motor.motor_asyncio import AsyncIOMotorClient
4|from dotenv import load_dotenv
5|from pydantic import BaseModel, Field
6|from typing import List, Optional
7|from datetime import datetime, timedelta
8|from pathlib import Path
9|import os
10|import uuid
11|import logging
12|
13|# Load environment variables
14|ROOT_DIR = Path(__file__).parent
15|load_dotenv(ROOT_DIR / '.env')
16|
17|# MongoDB connection
18|mongo_url = os.environ['MONGO_URL']
19|client = AsyncIOMotorClient(mongo_url)
20|db = client[os.environ['DB_NAME']]
21|
22|# Create the main app without a prefix
23|app = FastAPI()
24|
25|# Create a router with the /api prefix
26|api_router = APIRouter(prefix="/api")
27|
28|# Models
29|class TaskCreate(BaseModel):
30|    title: str
31|    description: Optional[str] = ""
32|    category: str
33|    priority: str = "medium"  # low, medium, high
34|    due_date: Optional[datetime] = None
35|    image: Optional[str] = None  # base64 encoded image
36|
37|class TaskUpdate(BaseModel):
38|    title: Optional[str] = None
39|    description: Optional[str] = None
40|    category: Optional[str] = None
41|    priority: Optional[str] = None
42|    due_date: Optional[datetime] = None
43|    completed: Optional[bool] = None
44|    image: Optional[str] = None  # base64 encoded image
45|
46|class Task(BaseModel):
47|    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
48|    title: str
49|    description: Optional[str] = ""
50|    category: str


