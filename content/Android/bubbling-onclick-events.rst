Bubbling OnClick events
#######################
:date: 2012-05-11
:tags: android,events,onclick
:category: Android

Today, I ran into a problem where I needed to bubble up the OnClick event. Inside of a RelativeLayout, I had a TextView which I had to make clickable (so that it could get some animation) because of this, the OnClickevent got swallowed up. To get around this, in the constructor, I create an `OnClickListener <http://developer.android.com/reference/android/view/View.OnClickListener.html>`_ which would simply call `performClick() <http://developer.android.com/reference/android/view/View.html#performClick()>`_ from the parent.

Here's how it goes

.. code-block:: java

    final View parent = this;
    mTitleView = (TextView) findViewById(R.id.TitleView);
    mTitleView.setOnClickListener(new OnClickListener() {
        @Override
        public void onClick(View v) {
            parent.performClick();
        }
    });

