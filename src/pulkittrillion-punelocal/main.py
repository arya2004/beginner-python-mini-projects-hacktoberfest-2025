def main():
    print("🛺 PuneLocal: Auto Rickshaw Fare Estimator")
    print("-" * 45)
    
    try:
        km = float(input("Enter distance in kilometers: "))
        if km <= 0:
            print("❌ Distance must be positive!")
            return

        # 🧠 Maharashtra Urban Ride Pricing Logic (MURPL)
        base_fare = 25      # First 1.5 km (Pune standard)
        rate_per_km = 16    # Approx after base (2024 Pune avg)

        if km <= 1.5:
            total = base_fare
        else:
            extra_km = km - 1.5
            total = base_fare + (extra_km * rate_per_km)

        # Add 10% buffer for traffic/waiting (realistic!)
        final_fare = round(total * 1.1)

        print(f"\n✅ Estimated Fair Fare: ₹{int(final_fare)}")
        print("💡 Tip: Always confirm fare before ride!")
        print("📍 Based on 2024 Pune auto rates + traffic buffer")

    except ValueError:
        print("❌ Please enter a valid number.")

if __name__ == "__main__":
    main()
