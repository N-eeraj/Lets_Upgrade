import Card from "./Card";

function Services()
{

    const service_list = [
        {
            title: "Web Dev",
            img: "https://img.freepik.com/free-vector/web-developers-courses-computer-programming-web-design-script-coding-study-computer-science-student-learning-interface-structure-components_335657-2542.jpg?size=338&ext=jpg",
            sub: "MERN Stack",
            desc: `MERN stands for MongoDB, Express, React, Node, after the four key technologies that make up the stack.
                    MongoDB, Express(.js), React(.js), Node(.js)`
        },

        {
            title: "App Dev",
            img: "https://img.freepik.com/free-vector/app-development-illustration_52683-47931.jpg?size=626&ext=jpg",
            sub: "Flutter",
            desc: `Flutter is an UI software development kit used to develop cross platform 
                    applications for Android, iOS, Linux, Mac, Windows, Google Fuchsia, and the web from a single codebase.`
        },
        
        {
            title: "Data Scientist",
            img: "https://png.pngtree.com/png-vector/20190721/ourlarge/pngtree-data-science-isometric-illustration-concept-of-web-page-design-for-website-png-image_1568016.jpg",
            sub: "Python",
            desc: `Data science uses scientific methods, processes, algorithms and systems to extract knowledge 
                    and insights from data, and apply knowledge and actionable insights from data`
        },
        
        {
            title: "Software Engineer",
            img: "https://content.techgig.com/thumb/msid-78956017,width-860,resizemode-4/How-to-become-a-software-engineer-in-2021.jpg?85576",
            sub: "C/C++, Java",
            desc: `Software engineering is the systematic application of engineering approaches to the development of software.`
        },
        
        {
            title: "Game Dev",
            img: "https://s3-us-west-2.amazonaws.com/robogarden-new/Articles/upload/blogs/lg-game-development-using-unity.jpg",
            sub: "Unity, C#",
            desc: `Unity is a cross-platform game engine developed by Unity Technologies, first announced in June 2005 at 
                    Apple Inc.'s Worldwide Developers Conference as a Mac OS X-exclusive game engine.`
        }
    ]

    return(

        <div className="services">
            {
                service_list.map((data) => (<Card title={data.title} img={data.img} sub={data.sub} desc={data.desc}/>))
            }
        </div>

    )

}

export default Services;