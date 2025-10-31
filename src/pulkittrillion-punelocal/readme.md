# PuneLocal: Auto Rickshaw Fare Estimator

A smart CLI tool that estimates **fair auto rickshaw fares in Pune** (and similar Indian cities) using the **Maharashtra Urban Ride Pricing Logic (MURPL)**.

## 💡 Real-Life Use
- Tourists & students avoid overcharging
- Locals verify if quoted fare is reasonable
- Works even when meters are “broken” 😏

## 🧠 How MURPL Works
- Base fare: ₹25 for first 1.5 km (Pune govt rate)
- ₹16/km after that (2024 avg)
- +10% buffer for traffic/waiting time
- No internet needed — pure logic!

## How to Run
```bash
cd src/pulkittrillion-punelocal
python main.py