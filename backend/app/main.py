# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1 import (albums, artists, customers, employees, genres,
                        invoice_lines, invoices, media_types, playlist_tracks,
                        playlists, tracks)

app = FastAPI(title="API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(playlist_tracks.router, prefix="/v1", tags=["PlaylistTracks"])
app.include_router(invoice_lines.router, prefix="/v1", tags=["InvoiceLines"])
app.include_router(media_types.router, prefix="/v1", tags=["MediaTypes"])
app.include_router(customers.router, prefix="/v1", tags=["Customers"])
app.include_router(playlists.router, prefix="/v1", tags=["Playlists"])
app.include_router(employees.router, prefix="/v1", tags=["Employees"])
app.include_router(invoices.router, prefix="/v1", tags=["Invoices"])
app.include_router(artists.router, prefix="/v1", tags=["Artists"])
app.include_router(tracks.router, prefix="/v1", tags=["Tracks"])
app.include_router(albums.router, prefix="/v1", tags=["Albums"])
app.include_router(genres.router, prefix="/v1", tags=["Genres"])
