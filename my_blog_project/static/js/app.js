const { useState, useEffect } = React;
const { createRoot } = ReactDOM;

const PostList = () => {
    const [posts, setPosts] = useState([]);
    const [search, setSearch] = useState('');
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        console.log('Fetching posts from API...');
        axios.get('/api/posts/')
            .then(response => {
                console.log('API Response:', response.data);
                setPosts(response.data);
                setLoading(false);
            })
            .catch(error => {
                console.error('Error fetching posts:', error);
                setError('Failed to load posts. Please try again later.');
                setLoading(false);
            });
    }, []);

    const filteredPosts = posts.filter(post =>
        post.title.toLowerCase().includes(search.toLowerCase()) ||
        post.content.toLowerCase().includes(search.toLowerCase())
    );

    return (
        <div>
            <h1 className="mb-4"><i className="fas fa-newspaper"></i> Blog Posts</h1>
            <div className="input-group mb-4">
                <input
                    type="text"
                    className="form-control"
                    placeholder="Search posts..."
                    value={search}
                    onChange={e => setSearch(e.target.value)}
                    aria-label="Search posts"
                />
                <button className="btn btn-primary" type="button">
                    <i className="fas fa-search"></i> Search
                </button>
            </div>
            {loading ? (
                <p>Loading posts...</p>
            ) : error ? (
                <p className="text-danger">{error}</p>
            ) : filteredPosts.length > 0 ? (
                filteredPosts.map(post => (
                    <div className="card mb-4" key={post.id}>
                        {post.image && (
                            <img
                                src={post.image}
                                className="card-img-top"
                                alt={post.title}
                                onError={() => console.error(`Failed to load image for post: ${post.title}`)}
                            />
                        )}
                        <div className="card-body">
                            <h5 className="card-title">
                                <a href={`/post/${post.slug}/`} className="text-decoration-none">
                                    {post.title}
                                </a>
                            </h5>
                            <p className="card-text">
                                {post.content.length > 100
                                    ? `${post.content.substring(0, 100)}...`
                                    : post.content}
                            </p>
                            <p className="text-muted">
                                <i className="fas fa-user"></i> By {post.author} |{' '}
                                <i className="fas fa-calendar-alt"></i>{' '}
                                {new Date(post.created_at).toLocaleDateString()}
                            </p>
                            <p className="text-muted">
                                <i className="fas fa-tags"></i> Tags:{' '}
                                {post.tags.length > 0 ? post.tags.join(', ') : 'No tags'}
                            </p>
                            <a href={`/post/${post.slug}/`} className="btn btn-primary">
                                Read More
                            </a>
                        </div>
                    </div>
                ))
            ) : (
                <p>No posts found.</p>
            )}
        </div>
    );
};

const root = createRoot(document.getElementById('react-post-list'));
root.render(<PostList />);
