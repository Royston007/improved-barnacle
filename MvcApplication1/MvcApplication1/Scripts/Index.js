function InitF() {
    console.log("Test")

    $('#tblEmpResults').DataTable({
        aaSorting: [0, 'asc']//,ajax: 'http://localhost:13906/'
    })

}

function AutoSync(url, data, parent_id, table_id, timeout) {

    var time = setInterval(function () {
        //var time = setTimeout(function () {
        var Init, lastSearch, lastSort, currPage;
        var isDataTable = $(table_id).hasClass("dataTable")
        if (isDataTable) {
            var oTable = $(table_id)
            //previous Init
            Init = oTable.DataTable().context[0].oInit
            //last search : 
            lastSearch = oTable.DataTable().context[0].oPreviousSearch.sSearch
            //last sort :
            lastSort = oTable.DataTable().context[0].aLastSort
            //paginate
            //$(table_id).dataTable().fnPageChange($(table_id).DataTable().page()+1)
            currPage = oTable.DataTable().page()
        }


        $.ajax({
            url: url,
            data: data,
            //async: false,
            success: function (d) {
                var l = $($(table_id).DataTable().rows().nodes())
                var dd = $(d.substr(d.indexOf("<table"), d.length)).find('tbody tr')
                var render = false
                if (l.length != dd.length) {
                    render = true;
                }
                else {
                    var counter = 0
                    for (var i = 0; i < l.length; i++) {

                        for (var j = 0; j < dd.length; j++) {
                            if ($(dd[j]).text().trim() == $(l[i]).text().trim()) {
                                counter += 1
                            }
                        }
                    }
                    console.log("Counter :" + counter)
                    render = (counter != l.length ? true : false);
                    //l.toArray().map(e=>$(e).text().trim())[0].toString() == $(dd[0]).text().trim().toString()
                }
                if (render) {
                    console.log(Init)
                    console.log(lastSearch)
                    console.log(lastSort)
                    console.log(currPage)
                    $(table_id).dataTable().fnDestroy()
                    //$(table_id).DataTable().fnDestroy()
                    $(parent_id).parent().html(d)
                    //$(table_id).dataTable().fnDestroy()
                    if (!$(table_id).hasClass("dataTable")) {
                        $(table_id).DataTable(Init)
                    }

                    $(table_id).dataTable().fnSort([lastSort[0].col, lastSort[0].dir])
                    $(table_id).DataTable().search(lastSearch).draw()
                    $(table_id).dataTable().fnPageChange(currPage)

                    //$(table_id).unbind('xhr.dt')

                    //			$(table_id).DataTable(Init)
                    //			$(table_id).DataTable().fnSort([lastSort[0].col, lastSort[0].dir])
                    //			$(table_id).DataTable().search(lastSearch).draw()
                    //			$(table_id).DataTable().fnPageChange(currPage)

                    //$(table_id+'_wrapper').remove()
                }
            },
            error: function (e) {
                console.log(e)
            }

        })
    },

     timeout)
    return time
}