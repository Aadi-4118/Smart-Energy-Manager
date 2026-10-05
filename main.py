print("====================================")
print("     SMART ENERGY MANAGER ⚡")
print("     SDG 7 - CLEAN ENERGY")
print("====================================")

print()

# Electricity rate
rate = 7

# AC
print("AC")
ac_power = 1500
ac_hours = float(input("AC is used for how many hours: "))

ac_units = (ac_power * ac_hours * 30) / 1000

# Fan
print("\nFan")
fan_power = 75
fan_hours = float(input("Fan is used for how many hours: "))

fan_units = (fan_power * fan_hours * 30) / 1000

# Light
print("\nLight")
light_power = 10
light_hours = float(input("Light is used for how many hours: "))

light_units = (light_power * light_hours * 30) / 1000

# TV
print("\nTV")
tv_power = 120
tv_hours = float(input("TV is used for how many hours: "))

tv_units = (tv_power * tv_hours * 30) / 1000

# Total consumption
total_units = ac_units + fan_units + light_units + tv_units

# Electricity bill
bill = total_units * rate

print()
print("====================================")
print("         ENERGY REPORT")
print("====================================")

print("AC:", round(ac_units, 2), "kWh/month")
print("Fan:", round(fan_units, 2), "kWh/month")
print("Light:", round(light_units, 2), "kWh/month")
print("TV:", round(tv_units, 2), "kWh/month")

print("------------------------------------")

print("Total Energy:", round(total_units, 2), "kWh/month")
print("Estimated Bill: ₹", round(bill, 2))

# Recommendation
print()
print("🤖 SMART RECOMMENDATION")

if ac_hours > 6:
    print("⚠️ Your AC usage is high.")
    print("Try reducing AC usage by 1 hour/day.")

elif ac_hours > 3:
    print("💡 Your AC usage is moderate.")
    print("You can save energy by reducing usage slightly.")

else:
    print("✅ Your AC usage is relatively low.")

print()
print("🌱 Use energy responsibly!")
print("SDG 7: Affordable and Clean Energy")
