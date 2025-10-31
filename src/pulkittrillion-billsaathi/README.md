# Billsaathi: The Smart Indian Dining Companion

A culturally-aware CLI tool that calculates **fair, region-informed tips** for Indian restaurants — accounting for **service charges**, **bill size**, and **local tipping norms** from Pune cafes to Delhi fine dining.

## 🇮🇳 Why Billsaathi?
In India, tipping isn’t one-size-fits-all:
- Many bills **already include 5–10% service charge**
- Small dhabas: ₹20–50 is generous
- Upscale restaurants: 10–15% expected if no service charge
- Over-tipping can confuse staff; under-tipping hurts livelihoods

Billsaathi solves this with the **Bharat Tip Optimization Logic (BTOL)** — a lightweight algorithm that adapts to real Indian billing practices.

## 🧠 Smart Features
- Detects if **service charge** is included
- Adjusts tip % based on **bill amount & regional norms**
- Suggests **per-person split** for group dinners
- Works offline — no APIs, no tracking

## How to Run
```bash
cd src/pulkittrillion-billsaathi
python main.py