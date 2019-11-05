test = {
  'name': 'q6',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> isinstance(answer6, list)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> all([isinstance(elt, str) for elt in answer6])
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> all([elt in calls['CVLEGEND'].values for elt in answer6])
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> set(answer6) == set(['LARCENY', 'BURGLARY - VEHICLE', 'VANDALISM', 'DISORDERLY CONDUCT', 'ASSAULT'])
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
