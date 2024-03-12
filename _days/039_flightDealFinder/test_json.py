my_json = {
  'id': '0a2b25c34d8300006b8ed259_0|25c30a2b4d980000d2e9d38f_0',
  'flyFrom': 'MAN',
  'flyTo': 'CDG',
  'cityFrom': 'Manchester',
  'cityCodeFrom': 'MAN',
  'cityTo': 'Paris',
  'cityCodeTo': 'PAR',
  'countryFrom': {
    'code': 'GB',
    'name': 'United Kingdom'
  },
  'countryTo': {
    'code': 'FR',
    'name': 'France'
  },
  'local_departure': '2024-04-30T20:25:00.000Z',
  'utc_departure': '2024-04-30T19:25:00.000Z',
  'local_arrival': '2024-04-30T22:55:00.000Z',
  'utc_arrival': '2024-04-30T20:55:00.000Z',
  'nightsInDest': 21,
  'quality': 107.255386,
  'distance': 588.85,
  'duration': {
    'departure': 5400,
    'return': 5100,
    'total': 10500
  },
  'price': 51,
  'conversion': {
    'EUR': 59.92217167349701,
    'GBP': 51
  },
  'fare': {
    'adults': 51,
    'children': 51,
    'infants': 51
  },
  'price_dropdown': {
    'base_fare': 51,
    'fees': 0
  },
  'bags_price': {
    '1': 94.874,
    '2': 206.67399999999998
  },
  'baglimit': {
    'hand_height': 45,
    'hand_length': 56,
    'hand_weight': 15,
    'hand_width': 25,
    'hold_dimensions_sum': 275,
    'hold_height': 90,
    'hold_length': 135,
    'hold_weight': 15,
    'hold_width': 50,
    'personal_item_height': 36,
    'personal_item_length': 45,
    'personal_item_weight': 15,
    'personal_item_width': 20
  },
  'availability': {
    'seats': 5
  },
  'airlines': [
    'U2'
  ],
  'route': [
    {
      'id': '0a2b25c34d8300006b8ed259_0',
      'combination_id': '0a2b25c34d8300006b8ed259',
      'flyFrom': 'MAN',
      'flyTo': 'CDG',
      'cityFrom': 'Manchester',
      'cityCodeFrom': 'MAN',
      'cityTo': 'Paris',
      'cityCodeTo': 'PAR',
      'local_departure': '2024-04-30T20:25:00.000Z',
      'utc_departure': '2024-04-30T19:25:00.000Z',
      'local_arrival': '2024-04-30T22:55:00.000Z',
      'utc_arrival': '2024-04-30T20:55:00.000Z',
      'airline': 'U2',
      'flight_no': 4646,
      'operating_carrier': 'EC',
      'operating_flight_no': '',
      'fare_basis': '',
      'fare_category': 'M',
      'fare_classes': '',
      'return': 0,
      'bags_recheck_required': False,
      'vi_connection': False,
      'guarantee': False,
      'equipment': None,
      'vehicle_type': 'aircraft'
    },
    {
      'id': '25c30a2b4d980000d2e9d38f_0',
      'combination_id': '25c30a2b4d980000d2e9d38f',
      'flyFrom': 'CDG',
      'flyTo': 'MAN',
      'cityFrom': 'Paris',
      'cityCodeFrom': 'PAR',
      'cityTo': 'Manchester',
      'cityCodeTo': 'MAN',
      'local_departure': '2024-05-21T18:30:00.000Z',
      'utc_departure': '2024-05-21T16:30:00.000Z',
      'local_arrival': '2024-05-21T18:55:00.000Z',
      'utc_arrival': '2024-05-21T17:55:00.000Z',
      'airline': 'U2',
      'flight_no': 2108,
      'operating_carrier': 'EC',
      'operating_flight_no': '',
      'fare_basis': '',
      'fare_category': 'M',
      'fare_classes': '',
      'return': 1,
      'bags_recheck_required': False,
      'vi_connection': False,
      'guarantee': False,
      'equipment': None,
      'vehicle_type': 'aircraft'
    }
  ],
  'booking_token': 'GM5Et1AwTMFeoD_eCwXM6jAIvN0jccOSu_69b4bCwT1GJ_S6p8EQgys6t3ZugXIo4Z_FFrolpLWDBupPYUaQ2iTkFCRyWwowupX3sU62lOR80uYpC1GhfgAFL_sSmewsyfvYVKNrocM58GhGwJyavvgope4_SBjWQUH8W-yyAqEAiDxhTxjZDeRst45kMTQTd5T7-XCE-fZHz2cr8HYRrNNOU3AyNzu5rPSQ5rc4tO-mej_X63YymzVXPY6tmqJ2bU4BJ8FyH2d2wU6UQWZHupGwQlXYpKUkZyKOuf0D0SWzFtEeOlC88gewJAiyt6FOdu12ydXzhvW_2_8QdzkXfC7eYLpUdaGpN1JuDXEwnFfm9rLIAtCrIt3jh82dBoTCmW7VHX51euv3XHkYaHzSHSSZyVR2qhiWRsQlgNxMFa9l1sdIxfOItY3csujINf08eEumaaVyk5p6ydm1POXZi3v3UA4Fsg6Z54n0-ui9IGSa5RxX_Edn4YxCvilmqpnYsm_Q2Z4bYXas24D6bnz8YIMdcqJBOaYcowdFASzcI08gUhx6oYHujwu277JRk2r9t6I4V3sLnRSFlW4gqzTV3j9NzypIdDEUg9SNIoCOMk-M=',
  'facilitated_booking_available': True,
  'pnr_count': 2,
  'has_airport_change': False,
  'technical_stops': 0,
  'throw_away_ticketing': False,
  'hidden_city_ticketing': False,
  'virtual_interlining': False
}

print(my_json["route"][1]["local_departure"])