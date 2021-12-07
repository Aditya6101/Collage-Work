import java.io.*;
import jakarta.servlet.*;
import jakarta.servlet.http.*;
 
public class DemoServlet extends HttpServlet{  
	public void doGet(HttpServletRequest req,HttpServletResponse res)  
	throws ServletException,IOException  
	{  

	res.setContentType("text/html");//setting the content type  
	PrintWriter pw=res.getWriter();//get the stream to write the data  
  
	pw.println("<html>");
	pw.println("<head>");
	pw.println("<title>First Servlet</title>");
	pw.println("</head>");
	pw.println("<body>");
	pw.println("<h1>This is my first servlet</h1>");
	pw.println("</body>");
	pw.println("<html>");
  		  
	pw.close();
}}  