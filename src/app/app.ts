import { JsonPipe } from '@angular/common';
import { HttpClient } from '@angular/common/http';
import { Component, effect, inject, signal } from '@angular/core';
import { tap } from 'rxjs';

export interface Post {
  userId: number;
  id: number;
  title: string;
  body: string;
}

@Component({
  selector: 'app-root',
  imports: [JsonPipe],
  templateUrl: './app.html',
  styleUrl: './app.scss'
})
export class App {
  private readonly http = inject(HttpClient);
  private readonly _loadPosts = this._loadPostsEffect();
  protected readonly title = signal('angular-20-zoneless');
  protected posts = signal<Post[]>([]);

  private _loadPostsEffect() {
    effect(() => {
      this.http.get<Post[]>('https://jsonplaceholder.typicode.com/posts').pipe(
        tap((posts) => {
          this.posts.set(posts);
        })
      ).subscribe();
    });
  }
}
