test = {
  'name': 'q5b',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> isinstance(answer5b, list)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> all([isinstance(elt, str) for elt in answer5b])
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(answer5b) == 3
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> all([elt in calls['OFFENSE'].values for elt in answer5b])
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> set([a.strip().upper() for a in answer5b]) == set(['THEFT FELONY (OVER $950)', 'THEFT FROM PERSON', 'THEFT MISD. (UNDER $950)'])
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
