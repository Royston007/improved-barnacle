using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using MvcApplication1.Models;

namespace MvcApplication1.Controllers
{


    public class HomeController : Controller
    {
        
        //
        // GET: /Home/
        static List<Employee> lst;

        public ActionResult Index()
        {

            return View();
        }

        public ActionResult GetDetails()
        {
            if (lst == null)
            {
                lst = new List<Employee>
                {
                    new Employee
                    {
                        EmployeeId = 3107,
                        EmployeeName = "Royston",
                        ProjectCode = 92741,
                        Designation = "Manager",
                        Active= "Y",

                    }
                };
            }
            ViewBag.Content = lst;
            return PartialView("GetDetails");
        }

        public ActionResult Add(Employee emp)
        {
            if (lst == null)
            {
                lst = new List<Employee>();
            }
            lst.Add(emp);
            return View();
        }

        public ActionResult Edit(Employee emp)  
        {
            lst.RemoveAt(lst.FindIndex(e => e.EmployeeName == emp.EmployeeName));
            
            lst.Add(emp);
            return View();

        }
    }
}
