Android Lifecycle for two activities
####################################
:date: 2012-01-24
:tags: android,activity-lifecycle
:category: Android

Today, I ran into some problems of not understanding how the lifecycle of two activities. When one activity starts another activity, when does the onPause_/onStop_/onDestroy_ run in comparison to the onCreate_/onStart_/onResume_ of the next activity. I put some logging in and here are the results:

| Activity\ **A**.\ onCreate_
| Activity\ **A**.\ onStart_
| Activity\ **A**.\ onResume_
| Activity\ **A**.\ onPause_
| Activity\ **B**.\ onCreate_
| Activity\ **B**.\ onStart_
| Activity\ **B**.\ onResume_
| Activity\ **A**.\ onStop_

For official docs about this, see: `Coordinating Activities <http://developer.android.com/guide/topics/fundamentals/activities.html#CoordinatingActivities>`_

.. _onPause: http://developer.android.com/reference/android/app/Activity.html#onPause()
.. _onStop: http://developer.android.com/reference/android/app/Activity.html#onStop()
.. _onDestroy: http://developer.android.com/reference/android/app/Activity.html#onDestroy()
.. _onCreate: http://developer.android.com/reference/android/app/Activity.html#onCreate()
.. _onStart: http://developer.android.com/reference/android/app/Activity.html#onStart()
.. _onResume: http://developer.android.com/reference/android/app/Activity.html#onResume()
