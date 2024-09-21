'use strict';
{
    const initData = JSON.parse(document.getElementById('django-admin-popup-response-constants').dataset.popupResponse);
    switch(initData.action) {
    case 'change':
        opener.dismissChangeRelatedObjectdopup(window, initData.value, initData.obj, initData.new_value);
        break;
    case 'delete':
        opener.dismissDeleteRelatedObjectdopup(window, initData.value);
        break;
    default:
        opener.dismissAddRelatedObjectdopup(window, initData.value, initData.obj);
        break;
    }
}
