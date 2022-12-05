#!/usr/bin/python3
# a dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'east' : 'Dining Room',
                  'item' : 'key'
                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'item' : 'monster'
                },
            'Dining Room' : {
                'north' : 'Pantry',
                'south' : 'Garden',
                'west' : 'Hall',
                'item' : 'potion'
            },
            'Pantry' : {
                'south' : 'Dining Room'
            },
            'Garden': {
                'north' : 'Dining Room'
            }

         }
