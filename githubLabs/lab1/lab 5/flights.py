

import json

class Flights:
    def __init__(self, filename):
        self.filename = filename
        self.data = []
        try:
            with open(filename, 'r') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            pass

    def add_flight(self, origin, destination, flight_number, departure, next_day, arrival):
        if not self._is_valid_time(departure) or not self._is_valid_time(arrival):
            return False
        
        self.data.append({
            'origin': origin,
            'destination': destination,
            'flight_number': flight_number,
            'departure': self._format_time(departure),
            'next_day': next_day,
            'arrival': self._format_time(arrival),
            'duration': self._calculate_duration(departure, arrival)
        })

        self._save_data()
        return True

    def get_flights(self):
        
        formatted_flights = []
        for flight in self.data:
            formatted_flights.append({
                'origin': flight['origin'],
                'destination': flight['destination'],
                'flight_number': flight['flight_number'],
                'departure': self._format_time(flight['departure']),
                'arrival': self._format_time(flight['arrival']),
                'duration': self._format_duration(flight['duration'])
            })
        return formatted_flights

    def _is_valid_time(self, time):
        try:
            if len(time) != 4:
                return False
            hour = int(time[:2])
            minute = int(time[2:])
            if hour < 0 or hour > 23 or minute < 0 or minute > 59:
                return False
        except ValueError:
            return False
        return True

    def _format_time(self, time):
        hour = int(time[:2])
        minute = int(time[2:])
        suffix = 'am'
        if hour >= 12:
            suffix = 'pm'
            if hour > 12:
                hour -= 12
        return f"{hour}:{minute:02d}{suffix}"

    def _calculate_duration(self, departure, arrival):
        departure_hour = int(departure[:2])
        departure_minute = int(departure[2:])
        arrival_hour = int(arrival[:2])
        arrival_minute = int(arrival[2:])
        minutes = (arrival_hour - departure_hour) * 60 + (arrival_minute - departure_minute)
        hours = minutes // 60
        minutes = minutes % 60
        return f"{hours}.{minutes:02d}"

    def _format_duration(self, duration):
        hours, minutes = duration.split('.')
        if hours == '1':
            hours_string = '1 hour'
        else:
            hours_string = f"{hours} hours"
        if minutes == '1':
            minutes_string = '1 minute'
        else:
            minutes_string = f"{minutes} minutes"
        return f"{hours_string} {minutes_string}"

    def _save_data(self):
        with open(self.filename, 'w') as file:
            json.dump(self.data, file)